from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Телефон', widget=forms.TextInput)
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class ClientCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтверждение пароля', strip=False, required=True, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone', 'password', 'password_confirm')
        labels = {
            'username': 'Логин',
            'email': 'Эл. почта',
            'phone': 'Телефон',
            'password': 'Пароль',
            'password_confirm': 'Подтверждение пароля'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class ClientUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone', 'avatar')
        labels = {
            'username': 'Логин',
            'email': 'Эл. почта',
            'phone': 'Телефон',
            'avatar': 'Фото'
        }


class PartnerCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтверждение пароля', strip=False, required=True, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'partner_category', 'password', 'password_confirm', 'avatar')
        labels = {
            'username': 'Логин',
            'email': 'Эл. почта',
            'phone': 'Телефон',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'partner_category': 'Тип заведения',
            'password': 'Пароль',
            'password_confirm': 'Подтверждение пароля',
            'avatar': 'Аватар',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class PartnerUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'partner_category', 'avatar')
        labels = {
            'username': 'Логин',
            'email': 'Эл. почта',
            'phone': 'Телефон',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'partner_category': 'Тип заведения',
            'avatar': 'Аватар',
        }


class AccountChangePasswordForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", strip=False, widget=forms.PasswordInput)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        appuser = self.instance
        appuser.set_password(self.cleaned_data["password"])
        if commit:
            appuser.save()
        return appuser

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']


