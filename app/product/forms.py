from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'groupa', 'image')
        labels = {
            'name': 'Наименование продукта',
            'price': 'Цена',
            'category': 'Категория продукта',
            'groupa': 'Группа',
            'image': 'Фото',
        }