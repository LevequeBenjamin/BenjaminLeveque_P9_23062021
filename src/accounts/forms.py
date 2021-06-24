from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username']
