// Получаем элементы формы и чекбокса
const form = document.getElementById('registration-form');
const checkbox = document.getElementById('thq-sign-up-4-terms');

// Добавляем обработчик события для отправки формы
form.addEventListener('submit', function (event) {
    // Если чекбокс не отмечен, отменяем отправку формы и выводим сообщение
    if (!checkbox.checked) {
        event.preventDefault();
        alert('Пожалуйста, согласитесь с условиями использования');
    }
});
