const background = document.querySelector('.head-section');

background.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX;
    const mouseY = e.clientY;

    const containerRect = background.getBoundingClientRect();

    const offsetX = (mouseX - containerRect.left) / containerRect.width;
    const offsetY = (mouseY - containerRect.top) / containerRect.height;

    const backgroundX = (offsetX - 0.5) * 50;
    const backgroundY = (offsetY - 0.5) * 50;

    background.style.backgroundPosition = `${50 + backgroundX}% ${50 + backgroundY}%`;
});

background.addEventListener('mouseleave', () => {
    background.style.backgroundPosition = '50% 50%';
});