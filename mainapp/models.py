from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя', unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя продукта', max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта',
                                  max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8,
                                decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количевство на складе',
                                           default=0)

    def __str__(self):
        return self.name, self.price, self.quantity, self.description, self.category
