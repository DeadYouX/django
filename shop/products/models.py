from django.db import models


class TypeProduct(models.Model):
    category_name = models.CharField(max_length=30, help_text='Категория товара: ')

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    SHIRT_currency = (
        ('D', 'Dollar'),
        ('E', 'Euro'),
        ('R', 'Rubles'),
    )
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    currency = models.CharField(max_length=1, choices=SHIRT_currency, verbose_name='Валюта')
    price = models.FloatField(verbose_name='Цена товара')
    size = models.CharField(max_length=100, verbose_name='Размер товара', null=True, blank=True)
    category = models.ForeignKey(TypeProduct, on_delete=models.SET_NULL, null=True, verbose_name='Категория',
                                 help_text='Выберите категорию товара', related_name='product')
    main_image = models.ImageField('Главное изображение товара', upload_to='media/')
    image1 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image2 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image3 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image4 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image5 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image6 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image7 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image8 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image9 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)
    image10 = models.ImageField('Дополнительное изображение товара', upload_to='media/', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
