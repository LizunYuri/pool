window.onscroll = function() {
    var scrollToTopBtn = document.getElementById("scrollToTopBtn");
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 20) {
      scrollToTopBtn.classList.add('to-top-block')
    } else {
        scrollToTopBtn.classList.remove('to-top-block')
    }
  };
  
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }