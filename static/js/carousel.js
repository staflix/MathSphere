let slideIndex = 0;
const slides = document.querySelectorAll('.carousel-slide');
const slideIndicators = document.querySelectorAll('.slide-indicator');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');
let autoSlideInterval;

function showSlide(n) {
    slides.forEach((slide, index) => {
        slide.style.transform = `translateX(${-100 * n}%)`;
        if (index === n) {
            slideIndicators[index].classList.add('active');
        } else {
            slideIndicators[index].classList.remove('active');
        }
    });
}

function nextSlide() {
    slideIndex = (slideIndex + 1) % slides.length;
    showSlide(slideIndex);
    resetAutoSlide();
}

function prevSlide() {
    slideIndex = (slideIndex - 1 + slides.length) % slides.length;
    showSlide(slideIndex);
    resetAutoSlide();
}

function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    autoSlideInterval = setInterval(() => {
        nextSlide();
    }, 10000);
}

prevButton.addEventListener('click', prevSlide);

nextButton.addEventListener('click', nextSlide);

showSlide(slideIndex);

resetAutoSlide();
