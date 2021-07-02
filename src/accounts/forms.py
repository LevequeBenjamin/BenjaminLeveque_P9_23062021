# django
from django.contrib.auth.forms import UserCreationForm

# models
from accounts.models import CustomUser


class UserRegisterForm(UserCreationForm):
    """UserRegisterForm inherits from UserCreationForm for creating CustomUser form."""
    class Meta:
        model = CustomUser
        fields = ['username']
