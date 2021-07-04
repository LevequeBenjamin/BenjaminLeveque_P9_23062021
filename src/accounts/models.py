"""Contains the models of accounts app."""

# django
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
