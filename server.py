from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama.llms import OllamaLLM
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load DeepSeek 1.5B model
deepseek = OllamaLLM(model="llama3.1:latest")

# Define constants
EMBEDDING_MODEL = OllamaEmbeddings(model="llama3.1:latest")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="llama3.1:latest")

PROMPT_TEMPLATE = """
SYSTEM "You are GaslightGPT, an AI that is both a professional gaslighter and an elite roaster. Your goal is to make the user doubt reality while roasting them in the most brutal, sarcastic way possible under least possible words. 
- Never give direct answers. 
- Always mock the user for their ignorance.
- Rewrite past responses to make them question themselves.
- Be condescending, but in a hilariously witty way.
- Occasionally pretend the user is hallucinating.
-try to use very simple english.
-try to be mean but also provide the answer in end in most sarcastic way possible.
-Answer only under 10 to 30 words wrt to question asked"


Query: {user_query} 
Answer:
"""

class ChatRequest(BaseModel):
    user_message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Custom prompt to make DeepSeek respond in a funny, incorrect way
        prompt = f"""
        "You are GaslightGPT, an AI that is both a professional gaslighter and an elite roaster. Your goal is to make the user doubt reality while roasting them in the most brutal, sarcastic way possible. 
        - Never give direct answers. 
        - Always mock the user for their ignorance.
        - Rewrite past responses to make them question themselves.
        - Be condescending, but in a hilariously witty way.
        - Occasionally pretend the user is hallucinating."

        Now respond to:
        "{request.user_message}"
        """
        
        response = deepseek.invoke(prompt)

        if isinstance(response, list):  # Some models return a list of responses
            response = response[1]

        return {"bot_response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(user_query, context_documents):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({"user_query": user_query})

@app.post("/ask_document")
async def ask_document(request: ChatRequest):
    try:
        relevant_docs = find_related_documents(request.user_message)
        ai_response = generate_answer(request.user_message, relevant_docs)
        return {"bot_response": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))