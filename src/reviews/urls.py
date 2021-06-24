from django.urls import path
from reviews.views import FluxView


app_name = "tickets"

urlpatterns = [
    path('', FluxView.as_view(), name='home'),
]
