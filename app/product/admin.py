from django.contrib import admin

from product.models import Product, Grouping


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'groupa', 'image', 'partner')
    list_filter = ('id', 'name', 'price', 'category', 'groupa', 'image', 'partner')
    search_fields = ('id', 'name', 'price', 'category', 'groupa', 'image', 'partner')
    readonly_fields = ('id',)


class GroupingAdmin(admin.ModelAdmin):
    list_display = ('name', 'at_partner')
    list_filter = ('id', 'name', 'at_partner')
    search_fields = ('id', 'name', 'at_partner')
    readonly_fields = ('id',)


admin.site.register(Product)
admin.site.register(Grouping)