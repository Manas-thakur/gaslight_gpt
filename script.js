const signupForm = document.getElementById("signupForm");

const canvas = document.getElementById("gameCanvas");

// Handle sign-up form submission
if (signupForm) {
    signupForm.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent default form submission

        const name = document.getElementById("name").value;
        const password = document.getElementById("password").value;
        const phone = document.getElementById("phone").value;

        // Simple validation
        if (name && password && phone) {
            alert("Sign-up successful!");
            // Here you can add further processing, like sending data to a server
            signupForm.reset(); // Reset the form after submission
        } else {
            alert("Please fill in all fields.");
        }
    });
}
const ctx = canvas.getContext("2d");
canvas.width = 400;
canvas.height = 300;

const startButton = document.getElementById("startButton");

// Draw pixelated player
const player = {
    x: 50,
    y: 150,
    size: 20,
    color: "#33FF33",
};

function drawPlayer() {
    ctx.fillStyle = player.color;
    ctx.fillRect(player.x, player.y, player.size, player.size);
}

// Game loop
function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPlayer();
    requestAnimationFrame(gameLoop);
}

startButton.addEventListener("click", () => {
    startButton.style.display = "none";
    gameLoop();
});

// Moving Twinkling Pixel Stars Effect
const starsCanvas = document.getElementById("starsCanvas");
const starsCtx = starsCanvas.getContext("2d");

starsCanvas.width = window.innerWidth;
starsCanvas.height = window.innerHeight;

let stars = [];
for (let i = 0; i < 100; i++) {
    stars.push({
        x: Math.random() * starsCanvas.width,
        y: Math.random() * starsCanvas.height,
        size: Math.random() * 3 + 1,
        speed: Math.random() * 0.3 ,
        brightness: Math.random()
    });
}

function drawStars() {
    starsCtx.clearRect(0, 0, starsCanvas.width, starsCanvas.height);
    for (let star of stars) {
        starsCtx.fillStyle = `rgba(51, 255, 51, ${star.brightness})`;
        starsCtx.fillRect(star.x, star.y, star.size, star.size);

        // Move stars downward
        star.y += star.speed;
        if (star.y > starsCanvas.height) {
            star.y = 0;
            star.x = Math.random() * starsCanvas.width;
        }
    }
    requestAnimationFrame(drawStars);
}

drawStars();
