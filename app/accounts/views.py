from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from accounts.forms import ClientCreationForm, PartnerCreationForm, LoginForm, AccountChangePasswordForm, \
    ClientUpdateForm, PartnerUpdateForm
from accounts.models import Account
from product.models import Product, Grouping


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        # print('Profile kwargs=', kwargs)
        id = kwargs['pk']
        groupa = kwargs.get('groupa')
        if groupa:
            groupa = kwargs['groupa']
        else:
            groupa=0
        CustUser = get_user_model()
        profile_owner = CustUser.objects.get(pk=id) # для определения владельца страницы, чтобы постронний пользователь не мог пользоваться его функционалом
        self.extra_context = {'profile_owner': profile_owner, 'id_groupa': groupa}
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class LoginView(SuccessMessageMixin, TemplateView):
    template_name = 'login.html'
    form = LoginForm
    success_message = 'Вы успешно зашли в систему'

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        appuser = authenticate(request=request, username=username, password=password)

        if not appuser:
            return redirect('login')

        # Login User(User)
        login(request, appuser)

        return redirect('home')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


# Create your views here.
class ClientRegisterView(CreateView):
    template_name = 'client_register.html'
    form_class = ClientCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            appuser = form.save()
            appuser.save()
            login(request, appuser)
            group = Group.objects.get(name='clients')
            appuser.groups.add(group)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class PartnerRegisterView(CreateView):
    template_name = 'partner_register.html'
    form_class = PartnerCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            appuser = form.save()
            appuser.user_type = 'partners'
            appuser.save()
            login(request, appuser)
            group = Group.objects.get(name='partners')
            appuser.groups.add(group)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


# @receiver(post_save, sender=Account)
# def add_user_to_group(sender, instance, created, **kwargs):
#     if created:
#         if instance.first_name != '_':
#             instance.user_type = 'partners'
#         print(f'{instance.user_type = }')
#         group = Group.objects.get(name=instance.user_type)  # Замените 'MyGroup' на имя вашей группы
#         instance.groups.add(group)


class ChangePasswordView(UpdateView):
    model = get_user_model()
    form_class = AccountChangePasswordForm
    template_name = 'change_password.html'
    context_object_name = 'user_obj'
    success_url = '/'


class ClientUpdateView(UpdateView):
    model = get_user_model()
    form_class = ClientUpdateForm
    template_name = 'client_update.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class PartnerUpdateView(UpdateView):
    model = get_user_model()
    form_class = PartnerUpdateForm
    template_name = 'partner_update.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})