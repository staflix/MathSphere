document.addEventListener('DOMContentLoaded', (event) => {
    const block = document.getElementById('top');
    const moveButton = document.getElementById('toggle-top');
    const close = document.getElementById('close_modal');
    const targetTop = 55; // Целевая координата Y

    // Функция для перемещения блока
    function moveDown() {
        block.style.top = `${targetTop}%`;
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
