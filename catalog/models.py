from django.db import models

from users.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название' )
    description = models.TextField(max_length=250, verbose_name='описание', help_text='Введите описание')
    image = models.ImageField(upload_to='media/photo', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузите фотографию')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='категория',
                                 help_text='Введите категорию', blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена', help_text='Введите цену')
    created_at = models.DateField(verbose_name='дата создания', help_text='Введите дату создания', blank=True,
                                  null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', blank=True, null=True)
    status_publication = models.BooleanField(default=False, verbose_name='статус публикации')
    owner = models.ForeignKey(CustomUser, help_text='Укажите владельца продукта', blank=True, null=True,
                              verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ["name"]
        permissions = [("can_unpublish_product", "Can unpublish product")]


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название', blank=True,
                            null=True)
    description = models.TextField(max_length=250, verbose_name='описание', help_text='Введите описание', blank=True,
                                   null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']
