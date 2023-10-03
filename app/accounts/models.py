from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import UserTypeChoice, PartnerCategoryChoice
from .managers import AccountManager


# Create your models here.
class Account(AbstractUser):
    username = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Имя',
        default='_'
    )
    last_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Фамилия',
        default='_'
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False,
        null=False
    )
    user_type = models.CharField(
        verbose_name='Тип пользователя',
        choices=UserTypeChoice.choices,
        max_length=250,
        default=UserTypeChoice.CLIENT
    )
    phone = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Телефон'
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар',
        default='user_pic/blank.jpg'
    )
    partner_category = models.CharField(
        verbose_name='Тип пользователя',
        choices=PartnerCategoryChoice.choices,
        max_length=250
    )

    objects = AccountManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
