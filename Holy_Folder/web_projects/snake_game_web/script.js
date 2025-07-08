const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const box = 20; // Size of each square
const canvasSize = 400;
let score = 0;

// Snake: initial position
let snake = [{ x: 9 * box, y: 10 * box }];
let direction = "RIGHT";

// Food: random initial position
let food = {
  x: Math.floor(Math.random() * (canvasSize / box)) * box,
  y: Math.floor(Math.random() * (canvasSize / box)) * box,
};

// Keyboard control
document.addEventListener("keydown", changeDirection);
function changeDirection(event) {
  if (event.key === "ArrowLeft" && direction !== "RIGHT") direction = "LEFT";
  else if (event.key === "ArrowUp" && direction !== "DOWN") direction = "UP";
  else if (event.key === "ArrowRight" && direction !== "LEFT") direction = "RIGHT";
  else if (event.key === "ArrowDown" && direction !== "UP") direction = "DOWN";
}

// Main Game Loop
function draw() {
  ctx.clearRect(0, 0, canvasSize, canvasSize);

  // Draw snake
  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i === 0 ? "#00ff00" : "#66ff66";
    ctx.fillRect(snake[i].x, snake[i].y, box, box);
  }

  // Draw food
  ctx.fillStyle = "#ff3333";
  ctx.fillRect(food.x, food.y, box, box);

  // Move snake head
  let headX = snake[0].x;
  let headY = snake[0].y;

  if (direction === "LEFT") headX -= box;
  if (direction === "RIGHT") headX += box;
  if (direction === "UP") headY -= box;
  if (direction === "DOWN") headY += box;

  // Check collision with wall
  if (
    headX < 0 || headX >= canvasSize ||
    headY < 0 || headY >= canvasSize ||
    collisionWithSelf(headX, headY)
  ) {
    clearInterval(game);
    alert("Game Over! Your score: " + score);
    return;
  }

  // Eat food
  if (headX === food.x && headY === food.y) {
    score++;
    document.getElementById("score").textContent = score;
    food = {
      x: Math.floor(Math.random() * (canvasSize / box)) * box,
      y: Math.floor(Math.random() * (canvasSize / box)) * box,
    };
  } else {
    snake.pop(); // remove tail
  }

  // Add new head
  const newHead = { x: headX, y: headY };
  snake.unshift(newHead);
}

function collisionWithSelf(x, y) {
  return snake.some((segment, index) => index !== 0 && segment.x === x && segment.y === y);
}

// Run game loop every 150ms
const game = setInterval(draw, 150);
