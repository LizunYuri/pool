const burgerBody = document.querySelector('.burger')
const toggleCenter = document.querySelector('.center')
const toggleTop = document.querySelector('.first')
const toggleBottom = document.querySelector('.last')
const bodyNav = document.querySelector('.body-nav')
const burgerButton = document.querySelector('.burger')
const navAnimation = document.querySelectorAll('.nav-animation')

let isOpen = false

const burgerClick = () => {

    if (isOpen) {
        toggleBottom.classList.remove('rotate-bottom')
        toggleTop.classList.remove('rotate-top')
        
        setTimeout(() => {
            toggleCenter.classList.remove('opacity-center')
            toggleTop.classList.remove('opacity-top')
            toggleBottom.classList.remove('opacity-bottom')
            burgerBody.style.zIndex = '1'
            burgerBody.style.position = 'relative'
            bodyNav.style.width = '0px'
            bodyNav.style.right = '-150px'

            isOpen = false
        }, 500)
        setTimeout(() => {
            navAnimation.forEach(e => {
                e.style.display = 'none'
                e.style.opacity = 0
            })
        }, 100)
    } else {
        toggleCenter.classList.add('opacity-center')
        toggleTop.classList.add('opacity-top')
        toggleBottom.classList.add('opacity-bottom')
        setTimeout(() => {
            toggleTop.classList.add('rotate-top')
            toggleBottom.classList.add('rotate-bottom')
            burgerBody.style.zIndex = '99'
            burgerBody.style.position = 'fixed'
            bodyNav.style.width = '300px'
            bodyNav.style.right = '0'
            isOpen = true
        },500)
        setTimeout(() => {
            navAnimation.forEach(e => {
                e.style.display = 'flex'
                e.style.opacity = 1
            })
        }, 1000)

    }
  
}


burgerButton.addEventListener('click', burgerClick);