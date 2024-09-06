const featursCards = document.querySelectorAll('.featurs-body-card');

const opacityEffect = (content, timing, effect, delay) => {
    content.forEach((e, index) => {
        const position = e.getBoundingClientRect();
        const positionCenter = position.top + (position.height * 0.3);

        if (positionCenter < window.innerHeight) {
            setTimeout(() => {
                e.classList.add(effect);
            }, timing + index * delay);
        }
    });
};

const handleScroll = () => {
    opacityEffect(featursCards, 1000, 'opacity-card', 500); 
};

window.addEventListener('DOMContentLoaded', () => {
    handleScroll();
    window.addEventListener('scroll', handleScroll);
});
