
const elements = document.querySelectorAll('.shop-content');
const blocks = document.querySelectorAll('.shop-list .block');
const servicesCard = document.querySelectorAll('.services-description-content')
const servicesCardImage = document.querySelectorAll('.services-description-img')
const catalogContent = document.querySelectorAll('.catalog-content')
const catalogText = document.querySelectorAll('.catalog-price')
const catalogImg = document.querySelectorAll('.catalog-img')

const positionBlocks = () => {
    elements.forEach((element, index) => {
        
        if ((index + 1) % 2 === 0) {

            element.style.flexDirection = 'row-reverse';

        }
    });



    blocks.forEach((block, index) => {
        
        if ((index + 1) % 2 === 0) {
            block.style.right = 0;
            block.style.transform = 'translateX(50%)'
        }
    });
    
    
    const lastBlock = blocks[blocks.length - 1]; // получаем последний элемент

    if (lastBlock) {
        lastBlock.style.display = 'none';
        
    }
}
// Анимация и отображение блоков каталога товаров

const shopBlockRewerse = () => {
    catalogContent.forEach((e, index) => {
        if((index + 1) % 2 === 0) {
            e.style.flexDirection = 'row-reverse';
        }
    })
}

const catalogEffect = (blockEffect, timing, effect, delay, percent) => {
    

    blockEffect.forEach((e) => {
        const position = e.getBoundingClientRect();
        const positionCenter = position.top + (position.height * percent);

        if (positionCenter < window.innerHeight) {
            setTimeout(() => {
                e.classList.add(effect);

                // Здесь изменяем ширину псевдоэлемента
                e.style.setProperty('--before-width', '100%');

                setTimeout(() => {
                    e.style.setProperty('--before-width', '0'); // Или другое значение, если нужно
                }, 500);
            }, timing);
        }
    });
};

const addReverseEffect = () => {
    servicesCard.forEach((e, index) => {
        if ((index + 1) % 2 === 0) {
            e.classList.add('reverse-content');
            
            // Найдем изображение внутри этого блока и добавим класс
            const img = e.querySelector('.services-description-img');
            if (img) {
                img.classList.add('reverse-img');
            }
        }
    });
}

const scrollCatalogEffect = () => {
    catalogEffect(
        catalogText,
        500,
        'catalog-animation-price',
        100,
        0.1
    ),
    catalogEffect(
        catalogImg,
        500,
        'catalog-animation-price',
        100,
        0.1
    )
}


window.addEventListener('DOMContentLoaded', () => {
    positionBlocks()
    addReverseEffect()
    shopBlockRewerse()
    scrollCatalogEffect()
    window.addEventListener('scroll', scrollCatalogEffect)
})


