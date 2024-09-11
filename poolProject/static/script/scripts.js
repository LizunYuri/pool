
const elements = document.querySelectorAll('.shop-content');
const blocks = document.querySelectorAll('.shop-list .block');


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


window.addEventListener('DOMContentLoaded', () => {
    positionBlocks()
})


