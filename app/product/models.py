from django.contrib.auth import get_user_model
from django.db import models

from product.choices import ProductCategoryChoice


class Grouping(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    at_partner = models.ManyToManyField(
        to=get_user_model(),
        related_name='partner_groups',
        verbose_name='Группы товаров',
    )

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name='Цена'
    )
    category = models.CharField(
        verbose_name='Тип продукта',
        choices=ProductCategoryChoice.choices,
        max_length=100,
        default=ProductCategoryChoice.FASTFOOD
    )
    groupa = models.ForeignKey(
        Grouping,
        null=True,
        blank=True,
        related_name='product',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images',
        verbose_name='Фото',
        default='images/blank.jpg'
    )
    partner = models.ForeignKey(
        to=get_user_model(),
        null=True,
        blank=True,
        related_name='partner_products',
        verbose_name='Товар партнера',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.PositiveSmallIntegerField(
        verbose_name='номер заказа'
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    supplier = models.ForeignKey(
        to=get_user_model(),
        related_name='partner_orders',
        verbose_name='Наименование партнера',
        on_delete=models.CASCADE
    )
    client = models.OneToOneField(
        to=get_user_model(),
        related_name='client_orders',
        verbose_name='Наименование заказчика',
        on_delete=models.CASCADE
    )
    total_amount = models.PositiveIntegerField(
        verbose_name='Сумма заказа'
    )


class Bill(models.Model):
    order_number = models.OneToOneField(
        to=Order,
        related_name='order_bill',
        verbose_name='Продукты по заказу',
        on_delete=models.CASCADE
    )
    product = models.OneToOneField(
        to=Product,
        related_name='bills_product',
        verbose_name='Наименование продуктов',
        on_delete=models.CASCADE
    )
    price = models.OneToOneField(
        to=Product,
        related_name='product_price',
        verbose_name='Цена продукта',
        on_delete=models.CASCADE
    )
    qty = models.PositiveIntegerField(
        verbose_name='Количество продуктов',
    )
    summary = models.PositiveIntegerField(
        verbose_name='Сумма по продукту',
    )


