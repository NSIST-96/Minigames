const dino = document.getElementById("dino");
const cactus = document.getElementById("cactus");
scoreBlock = document.querySelector(".game-score .score-count");

// очки
let score = 0;

function jump() {
  if (dino.classList != "jump") {
    dino.classList.add("jump");

    setTimeout(function () {
      dino.classList.remove("jump");
    }, 350);
  }
}

// показываем надпись Game Over
function showGameOver() {
    // прекращаем всю анимацию игры
    cancelAnimationFrame(rAF);
    // ставим флаг окончания
    gameOver = true;
    // рисуем чёрный прямоугольник посередине поля
    context.fillStyle = 'black';
    context.globalAlpha = 0.75;
    context.fillRect(0, canvas.height / 2 - 30, canvas.width, 60);
    // пишем надпись белым моноширинным шрифтом по центру
    context.globalAlpha = 1;
    context.fillStyle = 'white';
    context.font = '36px monospace';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.fillText('GAME OVER!', canvas.width / 2, canvas.height / 2);
  }

// Переменная выживаемости дино
let isAlive = setInterval(function () {
  // Вычисляем положение дино
  let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("top"));

  // Вычисляем положение кактуса
  let cactusLeft = parseInt(
    window.getComputedStyle(cactus).getPropertyValue("left")
  );


  // обнаруживаем столкновение
  if (cactusLeft < 50 && cactusLeft > 0 && dinoTop >= 149) {
    // столкновение - выводим надпись "конец игры"
    score = 0;
    drawScore();
    alert("КОНЕЦ ИГРЫ");
    
  }
  else{
    score++;
    drawScore();
  }
}, 100);

document.addEventListener("keydown", function (event) {
  jump();
});

//отрисовываем счёт
function drawScore() {
	scoreBlock.innerHTML = score;
}