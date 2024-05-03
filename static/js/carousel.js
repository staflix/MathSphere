document.addEventListener("DOMContentLoaded", function() {
  const slides = document.querySelectorAll(".carousel-slide");
  let currentSlide = 0;
  const slideInterval = setInterval(nextSlide, 5000);

  function nextSlide() {
    slides[currentSlide].classList.remove("show");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("show");
  }
});