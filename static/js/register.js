document.addEventListener('DOMContentLoaded', (event) => {
    const block = document.getElementById('policy');
    const moveButton = document.getElementById('policy-text');
    const close = document.getElementById('close_modal');
    const targetTop = 20; // Целевая координата Y

    // Функция для перемещения блока
    function moveDown() {
        block.style.top = `${targetTop}px`;
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
