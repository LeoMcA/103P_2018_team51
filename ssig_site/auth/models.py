from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, upi, email='', department='', full_name='',
                    given_name=''):
        if not upi:
            raise ValueError('Users must have a upi')

        user = self.model(
            upi=upi,
            email=email,
            department=department,
            full_name=full_name,
            given_name=given_name
        )

        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, upi, email='', department='', full_name='',
                         given_name='', password=None):
        user = self.create_user(
            upi=upi,
            email=email,
            department=department,
            full_name=full_name,
            given_name=given_name
        )
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    upi = models.CharField(max_length=254, unique=True, blank=False)
    email = models.EmailField(null=True)
    department = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254)
    given_name = models.CharField(max_length=254)

    objects = UserManager()

    USERNAME_FIELD = 'upi'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.upi

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.given_name

    @property
    def is_staff(self):
        return self.is_superuser
