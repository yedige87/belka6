from django.urls import path

from accounts.views import LoginView, LogoutView, ClientRegisterView, PartnerRegisterView, ProfileView, \
    ChangePasswordView, ClientUpdateView, PartnerUpdateView

urlpatterns = [
    path('accounts/<int:pk>/profile', ProfileView.as_view(), name='profile'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/client/register', ClientRegisterView.as_view(), name='client_register'),
    path('accounts/partner/register', PartnerRegisterView.as_view(), name='partner_register'),
    path('accounts/<int:pk>/change_password', ChangePasswordView.as_view(), name='change_password'),
    path('accounts/<int:pk>/client_update', ClientUpdateView.as_view(), name='client_update'),
    path('accounts/<int:pk>/partner_update', PartnerUpdateView.as_view(), name='partner_update'),
    path('accounts/<int:pk>/<int:groupa>/profile', ProfileView.as_view(), name='profile'),
]


