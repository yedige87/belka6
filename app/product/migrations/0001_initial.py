# Generated by Django 4.2.5 on 2023-09-28 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена')),
                ('category', models.CharField(choices=[('fastfood', 'еда'), ('medicines', 'лекарства'), ('food', 'полуфабрикаты')], default='fastfood', max_length=100, verbose_name='Тип продукта')),
                ('image', models.ImageField(blank=True, default='images/blank.jpg', null=True, upload_to='images', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAtPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='at_partner',
            field=models.ManyToManyField(related_name='partner_products', through='product.ProductAtPartner', to=settings.AUTH_USER_MODEL, verbose_name='Товар партнера'),
        ),
        migrations.AddField(
            model_name='product',
            name='groupa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.grouping'),
        ),
    ]
