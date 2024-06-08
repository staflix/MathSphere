document.addEventListener('DOMContentLoaded', (event) => {
    const block = document.getElementById('history');
    const moveButton = document.getElementById('attempts-history');
    const close = document.getElementById('close_modal');
    const targetTop = 20; // Целевая координата Y

    // Функция для перемещения блока
    function moveDown() {
        block.style.top = `calc(50% - 35vh)`;
    }
    function moveUp() {
        block.style.top = `-100vh`;
    }
    // Добавляем обработчик для кнопки
    moveButton.addEventListener('click', () => {
        moveDown();
    });
    close.addEventListener('click', () => {
        moveUp();
    });

});
