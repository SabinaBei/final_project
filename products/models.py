from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    class Meta:
        ordering = ('name',)
        index_together = (('id'),)

    def __str__(self):
        return self.name

# настройка комментариев
class ProductComment(models.Model):
    product = models.ForeignKey('products.Product', models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    text = models.TextField()


# настройка лайков
class ProductLike(models.Model):
    product = models.ForeignKey('products.Product', models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, models.SET_NULL, null=True)
