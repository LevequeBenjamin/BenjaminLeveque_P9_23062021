from django.urls import path, include

from accounts.views import SignUpView

app_name = "accounts"

urlpatterns = [
    path('nouveau/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
