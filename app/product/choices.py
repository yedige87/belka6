from django.db.models import TextChoices


class ProductCategoryChoice(TextChoices):
    FASTFOOD = 'fastfood', 'еда'
    MEDICINES = 'medicines', 'лекарства'
    FOOD = 'food', 'полуфабрикаты'