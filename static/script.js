document.addEventListener('DOMContentLoaded', () => {
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const imagesContainer = document.querySelector('.carousel-images');
    const images = document.querySelectorAll('.carousel-images img');
    
    let index = 0;
    
    function updateCarousel() {
        const offset = -index * 300; // Ancho en porcentaje
        imagesContainer.style.transform = `translateX(${offset}%)`;
    }
    
    prevButton.addEventListener('click', () => {
        index = (index > 0) ? index - 1 : images.length - 1;
        updateCarousel();
    });
    
    nextButton.addEventListener('click', () => {
        index = (index < images.length - 1) ? index + 1 : 0;
        updateCarousel();
    });
});
