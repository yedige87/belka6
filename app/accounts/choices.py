from django.db.models import TextChoices


class UserTypeChoice(TextChoices):
    CLIENT = 'clients', 'Клиент'
    PARTNER = 'partners', 'Партнер'


class PartnerCategoryChoice(TextChoices):
    RESTAURANT = 'restaurant', 'ресторан'
    PHARMACY = 'pharmacy', 'аптека'
    SUPERMARKET = 'supermarket', 'супермаркет'