from django.db import models

class FirstPageTitleModel(models.Model):
    welcome = models.CharField(max_length=100,
                                help_text='не больше 100 символов, включая пробелы и знаки припенания',
                                verbose_name='Приветственный текст вверху заголовка')
    
    title = models.CharField(max_length=200,
                                help_text='не больше 200 символов, включая пробелы и знаки припенания',
                                verbose_name='Заголовок первой страницы')
    
    subtitle = models.CharField(max_length=500,
                                help_text='не больше 500, включая пробелы и знаки припенания',
                                verbose_name='Подзаголовок первой страницы')
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Контент первой страницы'
        verbose_name_plural = 'Управление заголовками первой страницы'


