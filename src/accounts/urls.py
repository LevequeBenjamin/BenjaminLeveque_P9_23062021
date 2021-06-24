from django.urls import path

from accounts.views import SignUpView

app_name = "accounts"

urlpatterns = [
    path('', SignUpView.as_view(), name='home'),
]
