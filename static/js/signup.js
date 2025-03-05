document.getElementById("signupForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const formData = new FormData();
    formData.append('name', document.getElementById("name").value);
    formData.append('phone', document.getElementById("phone").value);
    formData.append('password', document.getElementById("password").value);
    
    fetch('/signup', {
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
                window.location.href = '/signin';
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
            speed: Math.random() * 0.3,
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

initStars();
drawStars();