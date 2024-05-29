from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()
    username = None
    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()
