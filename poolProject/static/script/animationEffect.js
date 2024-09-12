const featursCards = document.querySelectorAll('.featurs-body-card');
const aboutIcons = document.querySelectorAll('.about-icon')
const aboutContent = document.querySelector('.about-content')
const aboutCube = document.querySelector('.about-image-cube')
const aboutImg = document.querySelector('.about-image-content-img')
const shopImg = document.querySelectorAll('.shop-img')
const shopTitle = document.querySelectorAll('.shop-title')
const shopList = document.querySelectorAll('.shop-list-block-item')
const shopTopSubtitle = document.querySelector('.shop-top-subtitle');
const shopTopTitle = document.querySelector('.shop-top-title');
const shopBtn = document.querySelectorAll('.shop-btn');
const reviewTitle = document.querySelector('.review-title')
const reviewSubtitle =  document.querySelector('.review-subtitle')
const reviewCard = document.querySelectorAll('.review-card')
const awesomeTitle = document.querySelector('.awesome-title')
const awesomeSubtitle = document.querySelector('.awesome-subtitle')
const awesomeCard =  document.querySelectorAll('.awesome-content-card')

const opacityEffect = (content, timing, effect, delay, percent) => {
    content.forEach((e, index) => {
        const position = e.getBoundingClientRect();
        const positionCenter = position.top + (position.height * percent);

        if (positionCenter < window.innerHeight) {
            setTimeout(() => {
                e.classList.add(effect);
            }, timing + index * delay);
        }
    });
};

const loadEffect = (content, timeout, effect, percent) => {
    const position = content.getBoundingClientRect();
    const positionElement = position.top + position.height * percent;

    if(positionElement > 0 && positionElement < window.innerHeight){ // Элемент виден на экране
        setTimeout(() => {
            content.classList.add(effect);
        }, timeout);
    }
};


const handleScroll = () => {
    opacityEffect(
        featursCards,
        600, 
        'opacity-card', 
        500,
        0.2
    );

    opacityEffect(
        aboutIcons, 
        700,
        'about-opacity',
        500,
        0.2
    );

    loadEffect(
        aboutContent, 
        600, 
        'about-opacity',
        0.3
    );

    loadEffect(
        aboutCube, 
        600, 
        'visible',
        0.3
    );

    loadEffect(
        aboutImg,
        700,
        'img-visible',
        0.3
    );

    opacityEffect(
        shopImg, 
        700,
        'about-opacity',
        100,
        0.1
    );

    opacityEffect(
        shopTitle, 
        800,
        'about-opacity',
        100,
        0.2
    );
    opacityEffect(
        shopList, 
        700,
        'about-opacity',
        100,
        0.1
    );

    loadEffect(
        shopTopSubtitle,
        800,
        'about-opacity',
        0.1
    );

    loadEffect(
        shopTopTitle,
        800,
        'about-opacity',
        0.1
    );

    opacityEffect (
        shopBtn,
        700,
        'about-opacity',
        200,
        0.1
    );

    loadEffect(
        reviewSubtitle,
        500,
        'about-opacity',
        0.1
    );

    loadEffect(
        reviewTitle,
        500,
        'about-opacity',
        0.1
    );

    opacityEffect(
        reviewCard, 
        700,
        'about-opacity',
        100,
        0.1
    );


    loadEffect(
        awesomeSubtitle,
        500,
        'about-opacity',
        0.1
    );

    loadEffect(
        awesomeTitle,
        500,
        'about-opacity',
        0.1
    );

    opacityEffect(
        awesomeCard, 
        900,
        'about-opacity',
        100,
        0.1
    );

};



window.addEventListener('DOMContentLoaded', () => {
    handleScroll();
    window.addEventListener('scroll', handleScroll);
});

