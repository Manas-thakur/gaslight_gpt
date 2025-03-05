document.getElementById("signinForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const formData = new FormData();
    formData.append('phone', document.getElementById("phone").value);
    formData.append('password', document.getElementById("password").value);
    
    fetch('/signin', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('input[name="csrf_token"]').value
        },
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const message = document.getElementById("message");
        message.textContent = data.message;
        message.style.color = data.success ? "#33FF33" : "#FF3333";
        
        if (data.success) {
            setTimeout(() => {
                window.location.href = '/main';
            }, 2000);
        }
    })
    .catch(error => {
        const message = document.getElementById("message");
        message.textContent = "❌ An error occurred. Please try again.";
        message.style.color = "#FF3333";
    });
});

// Stars animation
const starsCanvas = document.getElementById("starsCanvas");
const starsCtx = starsCanvas.getContext("2d");

// Handle window resize
window.addEventListener('resize', () => {
    starsCanvas.width = window.innerWidth;
    starsCanvas.height = window.innerHeight;
    initStars(); // Reinitialize stars on resize
});

starsCanvas.width = window.innerWidth;
starsCanvas.height = window.innerHeight;

let stars = [];

function initStars() {
    stars = [];
    for (let i = 0; i < 100; i++) {
        stars.push({
            x: Math.random() * starsCanvas.width,
            y: Math.random() * starsCanvas.height,
            size: Math.random() * 3 + 1,
            speed: Math.random() * 0.7,
            brightness: Math.random()
        });
    }
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

let currentPosition = { x: 0, y: 0 };
let spaceshipDirection = { x: 1, y: 1 };

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

initStars();
drawStars();