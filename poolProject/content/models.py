import os
from django.db import models
from django.core.exceptions import ValidationError

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
        verbose_name_plural = 'Управление баннером (информация первого экрана)'

class FirstPageAboutModel(models.Model):
    title = models.CharField(max_length=100,
                             help_text='не больше 100 символов, включая пробелы и знаки припенания',
                             verbose_name='Заголовок пункта "О нас"')
    
    subtitle = models.CharField(max_length=50,
                                help_text='не больше 50, включая пробелы и знаки припенания, распалагается под иконкой в блоке',
                                verbose_name='Заголовок иконки')
    
    description = models.CharField(max_length=500,
                                help_text='не больше 500, включая пробелы и знаки припенания',
                                verbose_name='Описание блока "О нас"')
    icon = models.ImageField(upload_to='content/icons',
                             verbose_name='Иконка',
                             help_text='Использовать без фона')
    
    
    class Meta: 
        verbose_name = 'Контент блока "о нас"'
        verbose_name_plural = 'Управление блоком "о нас"'

    def save(self, *args, **kwargs):
        if not self.pk and FirstPageAboutModel.objects.count() >= 3:
            raise ValidationError("Может быть только три записи.")
        super(FirstPageAboutModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.icon:
            
            try:
                if os.path.isfile(self.icon.path):
                    os.remove(self.icon.path)
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
        
        # Вызываем стандартное удаление объекта
        super().delete(*args, **kwargs)
    
    def get_icon_url(self):
        if self.icon:
            return self.icon.url
        return None

    def __str__(self):
        return self.title

class FirstPageAwesomeModel(models.Model):
    title = models.CharField(max_length=100,
                             help_text='не больше 100 символов, включая пробелы и знаки припенания',
                             verbose_name='Заголовок пункта "приемущества"')
    
    text = models.CharField(max_length=300,
                                help_text='не больше 300, включая пробелы и знаки припенания',
                                verbose_name='Описание')

    class Meta: 
        verbose_name = 'Контент блока "Наши приемущества"'
        verbose_name_plural = 'Управление блоком "Наши приемущества"'

    def save(self, *args, **kwargs):
        if not self.pk and FirstPageAwesomeModel.objects.count() >= 6:
            raise ValidationError("Может быть только три записи.")
        super(FirstPageAwesomeModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class AboutValuesModel(models.Model):
    title = models.CharField(max_length=100,
                             help_text='не больше 100 символов, включая пробелы и знаки припенания',
                             verbose_name='Заголовок пункта "О нас"')
    
    description = models.CharField(max_length=300,
                                help_text='не больше 500, включая пробелы и знаки припенания',
                                verbose_name='Описание блока "О нас"')
    icon = models.ImageField(upload_to='content/icons/values',
                             verbose_name='Иконка',
                             help_text='Использовать без фона')
    

    def delete(self, *args, **kwargs):
        if self.icon:
            
            try:
                if os.path.isfile(self.icon.path):
                    os.remove(self.icon.path)
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
        
        # Вызываем стандартное удаление объекта
        super().delete(*args, **kwargs)
    
    def get_icon_url(self):
        if self.icon:
            return self.icon.url
        return None

    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности компании( отображается на странице "О нас")'
