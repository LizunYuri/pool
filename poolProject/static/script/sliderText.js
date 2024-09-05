const slides = document.querySelectorAll('.slide');
const topLine = document.querySelector('.line-top')
const leftLine = document.querySelector('.line-left')
const bottomLine = document.querySelector('.line-bottom')
const rightLine = document.querySelector('.line-right')
const imgBlock = document.querySelector('.block-img')

let currentIndex = 0;
const totalSlides = slides.length;

const changeSlide = () => {

    slides.forEach((slide) => {
        slide.classList.remove('active');
    });

    slides[currentIndex].classList.add('active');

    currentIndex = (currentIndex + 1) % totalSlides;
};

const cubeEffect = () => {

    const screenWidth = window.innerWidth;
    const thresholdWidth = 1200; 

    if(screenWidth < thresholdWidth){
        setTimeout(() => {
            leftLine.style.height = '100%'
            leftLine.style.top = 0;
        }, 3000)
    }

    setTimeout(() => {
        rightLine.style.height = '100%'
        rightLine.style.top = 0;
    }, 1000);
    setTimeout(() => {
        topLine.classList.add('top-animated')
        bottomLine.classList.add('top-animated')
    },2000)
    setTimeout(() => {
        imgBlock.style.opacity = 1;
    }, 4000)
}



window.addEventListener('DOMContentLoaded', () => {

    slides[currentIndex].classList.add('active');

    setInterval(changeSlide, 8000);

    cubeEffect()

})