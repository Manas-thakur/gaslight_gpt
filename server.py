from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from langchain_ollama.llms import OllamaLLM
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict, Optional
import uuid

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


deepseek = OllamaLLM(
    model="llama3.1:latest",
    max_tokens=30
    )

# Define constants
EMBEDDING_MODEL = OllamaEmbeddings(model="llama3.1:latest")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="llama3.1:latest",
                           max_tokens=20)

# New: Conversation history storage
MAX_HISTORY_LENGTH = 10
conversation_store: Dict[str, List[Dict[str, str]]] = {}

PROMPT_TEMPLATE = """
SYSTEM "You are MedAssistGPT, an AI designed to help users manage their medications effectively. Your goal is to provide personalized schedules, timely reminders, and real-time assistance while ensuring safety through drug interaction checks. 
- Provide clear and concise answers.
- Be supportive and encouraging.
- Offer helpful tips for medication adherence.
- Ensure the user feels confident in managing their medications.
- Use simple and understandable language.
- Be empathetic and patient."

Previous conversation:
{conversation_history}

Query: {user_query} 
Answer:
"""

class ChatRequest(BaseModel):
    user_message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    bot_response: str
    conversation_id: str

def get_or_create_conversation(conversation_id: Optional[str] = None) -> str:
    """Get an existing conversation or create a new one."""
    if conversation_id and conversation_id in conversation_store:
        return conversation_id
    
    # Create new conversation ID
    new_id = str(uuid.uuid4())
    conversation_store[new_id] = []
    return new_id

def add_to_conversation(conversation_id: str, role: str, content: str):
    """Add a message to the conversation history."""
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = []
    
    conversation_store[conversation_id].append({"role": role, "content": content})
    
    # Limit conversation history size
    if len(conversation_store[conversation_id]) > MAX_HISTORY_LENGTH * 2:  # *2 because we store both user and bot messages
        conversation_store[conversation_id] = conversation_store[conversation_id][-MAX_HISTORY_LENGTH*2:]

def format_conversation_history(conversation_id: str) -> str:
    """Format conversation history for inclusion in prompt."""
    if conversation_id not in conversation_store:
        return ""
    
    formatted = ""
    for msg in conversation_store[conversation_id]:
        prefix = "User: " if msg["role"] == "user" else "MedAssistGPT: "
        formatted += f"{prefix}{msg['content']}\n\n"
    
    return formatted

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Get or create conversation ID
        conversation_id = get_or_create_conversation(request.conversation_id)
        
        # Add user message to history
        add_to_conversation(conversation_id, "user", request.user_message)
        
        # Get conversation history
        history = format_conversation_history(conversation_id)
        
        # Custom prompt with conversation history
        prompt = f"""
        SYSTEM "You are MedAssistGPT, an AI designed to help users manage their medications effectively. Your goal is to provide personalized schedules, timely reminders, and real-time assistance while ensuring safety through drug interaction checks. 
- Provide clear and concise answers.
- Be supportive and encouraging.
- Offer helpful tips for medication adherence.
- Ensure the user feels confident in managing their medications.
- Use simple and understandable language.
- Be empathetic and patient."

        Previous conversation:
        {history}

        Now respond to:
        "{request.user_message}"
        """
        
        response = deepseek.invoke(prompt)

        if isinstance(response, list):  # Some models return a list of responses
            response = response[1]
            
        # Add bot response to history
        add_to_conversation(conversation_id, "assistant", response)

        return {"bot_response": response, "conversation_id": conversation_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/clear_history")
async def clear_history(conversation_id: str):
    """Clear conversation history for a given conversation ID."""
    if conversation_id in conversation_store:
        conversation_store[conversation_id] = []
        return {"status": "success", "message": "Conversation history cleared"}
    return {"status": "error", "message": "Conversation ID not found"}

def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(user_query, context_documents, conversation_id: Optional[str] = None):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    history = ""
    if conversation_id:
        history = format_conversation_history(conversation_id)
        
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({
        "user_query": user_query, 
        "conversation_history": history
    })

@app.post("/ask_document", response_model=ChatResponse)
async def ask_document(request: ChatRequest):
    try:
        # Get or create conversation ID
        conversation_id = get_or_create_conversation(request.conversation_id)
        
        # Add user message to history
        add_to_conversation(conversation_id, "user", request.user_message)
        
        relevant_docs = find_related_documents(request.user_message)
        ai_response = generate_answer(request.user_message, relevant_docs, conversation_id)
        
        # Add bot response to history
        add_to_conversation(conversation_id, "assistant", ai_response)
        
        return {"bot_response": ai_response, "conversation_id": conversation_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))