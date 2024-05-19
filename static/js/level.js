document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.getElementById('backButton');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const dots = document.querySelectorAll('.progress .dot');

    let currentLevel = 0;

    function updateProgress() {
        dots.forEach((dot, index) => {
            dot.style.backgroundColor = index === currentLevel ? 'gray' : 'white';
        });
    }

    function goToPreviousLevel() {
        if (currentLevel > 0) {
            currentLevel--;
            updateProgress();
            // Здесь вы можете обновить содержимое уровня, например:
            // document.getElementById('question').textContent = 'Вопрос ' + (currentLevel + 1);
            // document.getElementById('questionImage').src = 'path-to-your-image' + currentLevel + '.jpg';
        }
    }

    function goToNextLevel() {
        if (currentLevel < dots.length - 1) {
            currentLevel++;
            updateProgress();
            // Здесь вы можете обновить содержимое уровня, например:
            // document.getElementById('question').textContent = 'Вопрос ' + (currentLevel + 1);
            // document.getElementById('questionImage').src = 'path-to-your-image' + currentLevel + '.jpg';
        }
    }

    backButton.addEventListener('click', goToPreviousLevel);
    prevButton.addEventListener('click', goToPreviousLevel);
    nextButton.addEventListener('click', goToNextLevel);

    // Инициализируем прогресс при загрузке страницы
    updateProgress();
});
