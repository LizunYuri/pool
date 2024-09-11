$(document).ready(function() {
    // Функция для загрузки записи по ID с анимацией
    function loadAboutDetail(aboutId) {
        // Сначала скрываем текущий контент
        $('#about-detail-container').addClass('hidden');

        // Даем время на анимацию скрытия, а затем выполняем AJAX-запрос
        setTimeout(function() {
            $.ajax({
                url: '/abouts/' + aboutId,  // URL для получения данных
                method: 'GET',
                success: function(response) {
                    // Обновляем содержимое блока и показываем его с анимацией
                    $('#about-detail-container').html(response).removeClass('hidden');
                },
                error: function() {
                    alert('Ошибка загрузки данных.');
                }
            });
        }, 500); // Ждем 500ms (время совпадает с transition в CSS)
    }

    // При загрузке страницы загружаем первую запись
    var firstAboutId = $('.about-link').first().data('id');  // Получаем ID первой записи
    if (firstAboutId) {
        loadAboutDetail(firstAboutId);  // Загружаем первую запись
    }

    // При клике на ссылку загружаем соответствующую запись
    $('.about-link').on('click', function(e) {
        e.preventDefault();
        var aboutId = $(this).data('id');  // Получаем ID выбранного элемента
        loadAboutDetail(aboutId);  // Загружаем выбранную запись с анимацией
    });
});

