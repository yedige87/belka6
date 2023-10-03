from django.core.handlers.wsgi import WSGIRequest
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Account
from product.forms import ProductForm
from product.models import Product, Grouping


# Create your views here.
class HomePageView(ListView):
    # model = Account
    queryset = Account.objects.filter(user_type='partners')
    template_name = 'index.html'
    context_object_name = 'partners'
    extra_context = {'foodgroups': Grouping.objects.all()}


def partner2group(id_group, id_partner):
    group = Grouping.objects.get(pk=id_group)
    partner = Account.objects.get(pk=id_partner)

    if not partner in group.at_partner.all():
        group.at_partner.add(partner)

    return


class CreateProductView(CreateView):
    model = Product
    template_name = 'create_product.html'
    form_class = ProductForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.user = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.partner = form.instance.user
        self.object = form.save()
        id_group = self.object.groupa_id
        id_partner = self.object.partner_id
        partner2group(id_group, id_partner)
        return super().form_valid(form)


# Метод обрабатывает сигнал (после создания продукта автоматически ставит владельцем продукта - текущего пользователя)
# чтобы не выбирать владельца из списка

# @receiver(post_save, sender=Product)
# def add_user_to_product(sender, instance, created, **kwargs):
#     if created:
#         user = instance.user  # Пользователь, переданный в аргументах или контексте
#         instance.at_partner.add(user)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    template_name = 'update_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('home')
    success_message = 'Продукт удален!'


def product_category(request: WSGIRequest, pk):
    partners = Account.objects.filter(user_type='partners')
    foodgroups = Grouping.objects.all()
    current_group = int(pk)
    group_name = Grouping.objects.get(pk=current_group)
    context = {'partners': partners, 'foodgroups': foodgroups, 'group_name': group_name}
    return render(request, 'foodgroup_partners.html', context=context)

# метод для заполнения таблицы - 'какие группы товаров у партнеров'
# def partner_groups(request):
#     products = Product.objects.all()
#
#     for product in products:
#         num_group = product.groupa_id
#         num_partner = product.partner_id
#         foodgroup = Grouping.objects.get(pk=num_group)
#         partner = Account.objects.get(pk=num_partner)
#
#         if not partner in foodgroup.at_partner.all():
#             foodgroup.at_partner.add(partner)
