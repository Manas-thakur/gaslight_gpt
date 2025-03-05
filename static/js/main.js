const starsCanvas = document.getElementById("starsCanvas");
const starsCtx = starsCanvas.getContext("2d");

let spaceshipDirection = {
    x: Math.random() > 0.5 ? 1 : -1,
    y: Math.random() > 0.5 ? 1 : -1
};

let currentPosition = { x: 0, y: 0 };
starsCanvas.width = window.innerWidth;
starsCanvas.height = window.innerHeight;

let stars = [];
for (let i = 0; i < 100; i++) {
    stars.push({
        x: Math.random() * starsCanvas.width,
        y: Math.random() * starsCanvas.height,
        size: Math.random() * 3 + 1,
        speed: Math.random() * 0.6,
        brightness: Math.random()
    });
}

function drawStars() {
    starsCtx.clearRect(0, 0, starsCanvas.width, starsCanvas.height);
    for (let star of stars) {
        starsCtx.fillStyle = `rgba(51, 255, 51, ${star.brightness})`;
        starsCtx.fillRect(star.x, star.y, star.size, star.size);
        star.y += star.speed;
        if (star.y > starsCanvas.height) {
            star.y = 0;
            star.x = Math.random() * starsCanvas.width;
        }
    }
    requestAnimationFrame(drawStars);
}

drawStars();

function moveSpaceship() {
    const spaceship = document.getElementById('spaceship');
    const padding = 50;
    const maxX = window.innerWidth - 80 - padding;
    const maxY = window.innerHeight - 80 - padding;
    let newX = currentPosition.x + (50 * spaceshipDirection.x);
    let newY = currentPosition.y + (50 * spaceshipDirection.y);
    if (newX <= padding || newX >= maxX) spaceshipDirection.x *= -1;
    if (newY <= padding || newY >= maxY) spaceshipDirection.y *= -1;
    currentPosition.x = newX;
    currentPosition.y = newY;
    spaceship.style.transition = "transform 3s linear";
    spaceship.style.transform = `translate(${newX}px, ${newY}px)`;
}

setInterval(moveSpaceship, 3000);

// Add this function before sendMessage()
function typeMessage(element, text, speed = 25) {
    let index = 0;
    element.textContent = '';
    
    return new Promise((resolve) => {
        function type() {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(type, speed);
            } else {
                resolve();
            }
        }
        type();
    });
}

// Modify the sendMessage function to use typing effect
async function sendMessage() {
    const userInput = document.getElementById("userInput");
    const chatbox = document.getElementById("chatbox");
    const message = userInput.value.trim();
    if (message === "") return;

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = message;
    chatbox.appendChild(userMessage);

    // Send request to backend
    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_message: message })
        });
        const data = await response.json();

        // Display bot response with typing effect
        const botMessage = document.createElement("div");
        botMessage.className = "message bot";
        chatbox.appendChild(botMessage);
        await typeMessage(botMessage, data.bot_response);
    } catch (error) {
        console.error("Error:", error);
    }

    userInput.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;
}