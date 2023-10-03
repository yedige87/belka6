from django.contrib.auth.models import UserManager


class AccountManager(UserManager):

    def create_user(self, email=None, password=None, **kwargs):
        if not email:   # не работает, т.к. поле и так обязательное для заполнения
            raise ValueError('Users must have an Email')

        user = self.model(
            email=email, **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user