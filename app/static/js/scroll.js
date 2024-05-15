window.addEventListener('scroll', function() {
    var scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
    var scrolled = window.scrollY;

    // Проверяем, достигли ли мы нижнего края страницы
    if (scrolled === scrollableHeight) {
        // Получаем элемент стилей ползунка
        var scrollbarStyle = document.createElement('style');
        scrollbarStyle.textContent = `
            body::-webkit-scrollbar-thumb {
                background-color: #5128f5;
            }
        `;
        document.head.appendChild(scrollbarStyle);
    }
});