const cycleObjectsCard = document.querySelectorAll('.cycle-objects-card')
const cycleObjectsSubtitle = document.querySelectorAll('.cycle-objects-subtitle')
const cycleObjectsTitle = document.querySelectorAll('.cycle-objects-title')
const cycleObjectsImg = document.querySelectorAll('.cycle-objects-img')


const cycleEffectCard = (content, timing, effect, delay, percent) => {
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

const cycleEffectFade = (content, timeout, effect, percent) => {
    content.forEach((e) => {
        const position = e.getBoundingClientRect();
        const positionElement = position.top + position.height * percent;

        if (positionElement < window.innerHeight) {
            setTimeout(() => {
                e.classList.add(effect);
            }, timeout);
        }
    });
};



const handleScrollEffect = () => {
    cycleEffectCard(
        cycleObjectsCard,
        300,
        'fade-element',
        100,
        0.1
        );
    
    cycleEffectFade(
        cycleObjectsSubtitle,
        500,
        'fade-element',
        0.1
    )
    cycleEffectFade(
        cycleObjectsTitle,
        600,
        'fade-element',
        0.1
    )
    cycleEffectFade(
        cycleObjectsImg,
        700,
        'fade-element',
        0.2
    )
}

window.addEventListener('DOMContentLoaded', () => {
    handleScrollEffect();
    window.addEventListener('scroll', handleScrollEffect);
});