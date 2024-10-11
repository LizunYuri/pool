document.addEventListener("DOMContentLoaded", function() {
    var reviews = document.querySelectorAll('.personal-card'); // Все отзывы
    var currentStartIndex = 0;
    var reviewsPerPage = 3; // Изначально 2 отзыва на страницу

    function updateReviewsPerPage() {
        if (window.innerWidth < 1200) {
            reviewsPerPage = 1; // Если ширина экрана меньше 768px, показываем 1 отзыв
        } else {
            reviewsPerPage = 3; // Если ширина экрана больше или равна 768px, показываем 2 отзыва
        }
    }

    function showReviews(startIndex) {
        reviews.forEach((review, index) => {
            if (index >= startIndex && index < startIndex + reviewsPerPage) {
                review.style.display = 'block'; // Показываем
            } else {
                review.style.display = 'none'; // Скрываем
            }
        });
    }

    // Обновляем количество отображаемых отзывов при изменении размера окна
    window.addEventListener('resize', function() {
        updateReviewsPerPage(); // Обновляем количество отзывов на основе ширины экрана
        showReviews(currentStartIndex); // Показать обновленное количество отзывов
    });

    // Изначально обновляем количество отзывов в зависимости от размера экрана
    updateReviewsPerPage();
    showReviews(currentStartIndex); // Показываем начальные отзывы

    // Обработчик кнопки "Следующий"
    document.getElementById('next-persona-btn').addEventListener('click', function() {
        if (currentStartIndex + reviewsPerPage < reviews.length) {
            currentStartIndex += 1; // Смещаемся на 1 запись вперед
            showReviews(currentStartIndex);
        }
    });

    // Обработчик кнопки "Предыдущий"
    document.getElementById('prev-persona-btn').addEventListener('click', function() {
        if (currentStartIndex > 0) {
            currentStartIndex -= 1; // Смещаемся на 1 запись назад
            showReviews(currentStartIndex);
        }
    });
});
