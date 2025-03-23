# GasLight GPT 🚀

GasLight GPT is a retro-themed chatbot application that allows users to interact with an AI in a fun and engaging way. The application features a space-themed interface with a spaceship and moon, and a chatbox where users can type their messages and receive responses from the bot.

<p align="center">
  <img src="static/images/spaceship.png" alt="GasLight GPT Logo" width="150">
</p>

## ✨ Features

- 🎮 Retro-themed user interface with nostalgic design elements
- 🌠 Space-themed graphics including an animated spaceship and moon
- 💬 Interactive chatbox for user input and AI-powered responses
- 🔄 Real-time conversation updates without page refresh
- 🔒 User authentication with secure logout functionality
- 📱 Responsive design that works on desktop and mobile devices

## 🗂️ Project Structure

```
/C:/2025/gaslight_chatgpt/
├── static/                  # Static assets
│   ├── css/
│   │   └── main.css         # Main stylesheet
│   ├── js/
│   │   └── main.js          # Client-side functionality
│   └── images/
│       ├── spaceship.png    # Spaceship graphic
│       └── moon.png         # Moon graphic
├── templates/
│   └── main.html            # Main application template
├── server.py                # FastAPI server implementation
├── app.py                   # Alternative Flask implementation
├── requirements.txt         # Python dependencies
└── README.md                # This documentation file
```

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/gaslight_chatgpt.git
    ```
2. Navigate to the project directory:
    ```sh
    cd gaslight_chatgpt
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Usage

### Starting the Server

1. Run the application using Uvicorn server (recommended):
    ```sh
    uvicorn app:app --reload
    ```
   
   For more control over the server configuration, you can specify port and host:
    ```sh
    uvicorn server:app --reload --port 8000 --host 0.0.0.0
    ```
   
   Alternatively, you can run the application directly:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to:
   - `http://localhost:8000` when using Uvicorn with default settings
   - `http://localhost:5000` when using the direct Python method
   - `http://your-server-ip:8000` when accessing from another device on the network

### Using the Application

1. Enter your message in the chatbox at the bottom of the screen
2. Press "Send" or hit Enter to submit your message
3. Wait for the AI to respond (typically within seconds)
4. Continue the conversation as desired
5. Use the logout button when finished

## 📂 File Descriptions

- `server.py`: FastAPI server implementation that handles requests and AI interactions
- `app.py`: Alternative Flask implementation of the server
- `main.html`: The main HTML template that defines the structure of the chatbot interface
- `main.css`: CSS stylesheet that creates the retro-themed design
- `main.js`: JavaScript that handles user interactions and communication with the server
- `spaceship.png` and `moon.png`: Vector graphics used in the space-themed interface
- `requirements.txt`: List of Python dependencies required to run the application

## 🔄 API Endpoints

- `POST /chat` - Send a message to the AI and receive a response
- `GET /history` - Retrieve conversation history
- `POST /logout` - End the current user session

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the project's style guidelines and includes appropriate tests.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to OpenAI for the underlying chatbot technology
- Space graphics inspired by retro sci-fi aesthetics
- Built with FastAPI and modern web technologies
