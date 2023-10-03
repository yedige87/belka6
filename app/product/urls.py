from django.urls import path

from product.views import HomePageView, CreateProductView, product_category, ProductDetailView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/add_product', CreateProductView.as_view(), name='add_product'),
    path('product/<int:pk>/product_category', product_category, name='product_category'),
    path('product/<int:pk>/detail_product', ProductDetailView.as_view(), name='detail_product'),
    path('product/<int:pk>/update_product', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete_product', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete'),
]