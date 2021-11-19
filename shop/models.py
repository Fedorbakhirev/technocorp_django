from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    available = models.PositiveIntegerField(default=0, verbose_name='Количество в наличии')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Order(models.Model):
    customer_username = models.CharField(max_length=255, verbose_name='Логин покупателя')
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(max_length=255, verbose_name='Эл. почта')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    address = models.CharField(max_length=500, verbose_name='Адрес')
    note = models.TextField(verbose_name='Комментарий к заказу')
    products = models.TextField(verbose_name='Товары')
    price = models.DecimalField(max_digits=15,decimal_places=2, verbose_name='Итоговая цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ №{}'.format(self.id)
