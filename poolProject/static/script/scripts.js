
const elements = document.querySelectorAll('.shop-content');
const blocks = document.querySelectorAll('.shop-list .block');
const servicesCard = document.querySelectorAll('.services-description-content')
const servicesCardImage = document.querySelectorAll('.services-description-img')


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



window.addEventListener('DOMContentLoaded', () => {
    positionBlocks()
    addReverseEffect()
})


