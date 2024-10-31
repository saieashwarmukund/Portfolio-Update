window.addEventListener('resize', () => {
    const carouselImages = document.querySelectorAll('#carouselExampleIndicators .carousel-item img');
    const maxHeight = 800; // Adjust the max height as needed

    carouselImages.forEach(img => {
        const width = img.parentElement.clientWidth;
        img.style.width = `${width}px`;
        img.style.height = `${Math.min(img.naturalHeight, maxHeight)}px`;
    });
});