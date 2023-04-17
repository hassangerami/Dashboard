from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import Manager


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return f'{self.email} - {self.full_name}'

    def is_staff(self):
        return self.is_admin
