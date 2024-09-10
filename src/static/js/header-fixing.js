const header = document.getElementById('header');

const headerOffsetTop = header.offsetTop;

window.onscroll = function() {
    if (window.scrollY > headerOffsetTop) {
        header.classList.add('header-fixed');
    } else {
        header.classList.remove('header-fixed');
    }
};