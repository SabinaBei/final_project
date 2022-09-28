### Всем привет, меня зовут Сабина и я новичок в мире Python.

# Это мой финальный проект - интернет-магазин "final_project"

### Python 3.8.10
### Django 4.1.1
### djangorestframework 3.13.1

## Основные модели данного проекта: Продукты и Категории
    
    class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    
    class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
#### В проекте реализовано: комментарии, лайки, рейтинг продуктов

#####
