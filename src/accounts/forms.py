from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class UserRegistration(UserCreationForm):
    class Meta:
        model = CustomUser
