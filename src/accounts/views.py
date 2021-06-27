# django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
# forms
from accounts.forms import UserRegisterForm


class SignUpView(SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegisterForm
    template_name = "accounts/signup.html"
    success_message = "Votre profil est créé avec succés"
