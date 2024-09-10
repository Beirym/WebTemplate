const navIcon = document.getElementById('nav-icon');
const slideMenu = document.getElementById('slideout-menu');
const closeIcon = document.getElementById('close-icon');
const links = document.getElementById('nav-links');


navIcon.addEventListener('click', () => {
    slideMenu.classList.add('open');
});

closeIcon.addEventListener('click', () => {
    slideMenu.classList.remove('open');
});
links.addEventListener('click', () => {
    slideMenu.classList.remove('open');
});
