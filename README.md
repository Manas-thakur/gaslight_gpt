<div align="center">

# 🌌 GasLight GPT 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-00a393.svg)](https://fastapi.tiangolo.com/)
[![Made with Love](https://img.shields.io/badge/Made%20with-Love-ff69b4.svg)](https://github.com/yourusername/gaslight_chatgpt)

<p align="center">
  <img src="static/images/spaceship.png" alt="GasLight GPT Logo" width="200">
</p>

**A retro-futuristic AI chatbot with cosmic vibes**

[Features](#-features) • 
[Installation](#-installation) • 
[Usage](#-usage) • 
[API](#-api-endpoints) • 
[Contributing](#-contributing)

</div>

---

## 🌟 Overview

GasLight GPT combines nostalgic retro aesthetics with cutting-edge AI technology, creating an immersive chat experience with a space-themed interface. Navigate the cosmic void of conversation with your trusty AI companion!

<details>
<summary>📸 Screenshot (click to expand)</summary>
<p align="center">
  <img src="https://via.placeholder.com/800x450.png?text=GasLight+GPT+Interface" alt="GasLight GPT Interface" width="800">
</p>
</details>

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎮 **Retro Interface** | Nostalgic design with pixel-perfect details |
| 🌠 **Space Theme** | Animated spaceship and cosmic elements |
| 💬 **Advanced AI** | Smart conversations with context awareness |
| 🔄 **Real-time Updates** | Instant responses without page refresh |
| 🔒 **User Authentication** | Secure login and session management |
| 📱 **Responsive Design** | Seamless experience across all devices |

## 🗂️ Project Structure

```
/C:/2025/gaslight_chatgpt/
├── 📁 static/                  # Static assets
│   ├── 📁 css/
│   │   └── 📄 main.css         # Main stylesheet
│   ├── 📁 js/
│   │   └── 📄 main.js          # Client-side functionality
│   └── 📁 images/
│       ├── 🖼️ spaceship.png    # Spaceship graphic
│       └── 🖼️ moon.png         # Moon graphic
├── 📁 templates/
│   └── 📄 main.html            # Main application template
├── 📄 server.py                # FastAPI server implementation
├── 📄 app.py                   # Alternative Flask implementation
├── 📄 requirements.txt         # Python dependencies
└── 📄 README.md                # This documentation file
```

## 🔧 Installation

### Prerequisites

<table>
  <tr>
    <td>✅ Python 3.8+</td>
    <td>✅ pip package manager</td>
    <td>✅ Internet connection</td>
  </tr>
</table>

### Setup Steps

<ol>
  <li>
    <strong>Clone the repository:</strong>
    <pre><code>git clone https://github.com/yourusername/gaslight_chatgpt.git</code></pre>
  </li>
  <li>
    <strong>Navigate to the project directory:</strong>
    <pre><code>cd gaslight_chatgpt</code></pre>
  </li>
  <li>
    <strong>Install the required dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

## 🚀 Usage

### Starting the Server

<div class="command-options">
  <div class="option">
    <h4>🔹 Using Uvicorn (Recommended)</h4>
    <pre><code>uvicorn app:app --reload</code></pre>
  </div>
  
  <div class="option">
    <h4>🔹 Advanced Configuration</h4>
    <pre><code>uvicorn server:app --reload --port 8000 --host 0.0.0.0</code></pre>
  </div>
  
  <div class="option">
    <h4>🔹 Alternative Method</h4>
    <pre><code>python app.py</code></pre>
  </div>
</div>

### 🌐 Access Points

- `http://localhost:8000` - Default Uvicorn
- `http://localhost:5000` - Default Flask
- `http://your-server-ip:8000` - Remote Access

### 🎮 Quick Start Guide

1. ⌨️ Type your message in the retro terminal interface
2. 🚀 Hit "Send" to transmit your thoughts across the cosmos
3. 🔭 Watch as the AI contemplates and responds
4. 🌌 Continue your interstellar conversation
5. 🚪 Use the logout portal when your journey is complete

## 📂 File Descriptions

<table>
  <tr>
    <th>File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>server.py</code></td>
    <td>Core FastAPI server with API routes and logic</td>
  </tr>
  <tr>
    <td><code>app.py</code></td>
    <td>Alternative Flask implementation for flexibility</td>
  </tr>
  <tr>
    <td><code>main.html</code></td>
    <td>HTML structure with retro-futuristic elements</td>
  </tr>
  <tr>
    <td><code>main.css</code></td>
    <td>Stylesheets defining the cosmic aesthetic</td>
  </tr>
  <tr>
    <td><code>main.js</code></td>
    <td>Interactive elements and real-time communication</td>
  </tr>
  <tr>
    <td><code>requirements.txt</code></td>
    <td>Required Python packages and dependencies</td>
  </tr>
</table>

## 🔄 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat` | POST | Transmit messages to the AI core |
| `/history` | GET | Access your conversation timeline |
| `/logout` | POST | Terminate your current session |

## 🤝 Contributing

<div align="center">

**Your contributions fuel our journey across the stars!**

</div>

1. 🍴 Fork the repository
2. 🌿 Create your feature branch: `git checkout -b cosmic-feature`
3. 💾 Commit your changes: `git commit -m 'Add cosmic feature'`
4. 🚀 Push to the branch: `git push origin cosmic-feature`
5. 🔍 Submit a pull request

<details>
<summary>Contribution Guidelines</summary>
<ul>
  <li>Follow the established code style</li>
  <li>Add tests for new features</li>
  <li>Update documentation accordingly</li>
  <li>Ensure all tests pass before submitting</li>
</ul>
</details>

## 📜 License

This project is protected by the [MIT License](LICENSE) - see the LICENSE file for celestial details.

---

<div align="center">

## 🙏 Acknowledgments

Powered by OpenAI technology • Inspired by retro sci-fi aesthetics • Built with FastAPI and cosmic code

<p>
  <img src="static/images/moon.png" alt="Moon" width="50">
  <br>
  <sub>© 2025 GasLight GPT - Voyage through the digital cosmos</sub>
</p>

</div>
