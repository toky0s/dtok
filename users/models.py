from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class DtokUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField('Profile picture', upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField(null=True, blank=False, max_length=10)
    display_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','display_name','is_active','is_staff']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
