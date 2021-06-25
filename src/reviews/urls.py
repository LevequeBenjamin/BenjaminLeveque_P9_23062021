from django.urls import path
from reviews.views import FluxView, TicketCreate, TicketUpdate, PostsView, TicketDelete

app_name = "flux"

urlpatterns = [
    path('', FluxView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('create-ticket/', TicketCreate.as_view(), name='create-ticket'),
    path('update-ticket/<int:pk>/', TicketUpdate.as_view(), name='update-ticket'),
    path('delete-ticket/<int:pk>/', TicketDelete.as_view(), name='delete-ticket'),
]
