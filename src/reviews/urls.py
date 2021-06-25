from django.urls import path
from reviews.views import FluxView, TicketCreate, TicketUpdate, PostsView, TicketDelete, ReviewDelete

app_name = "flux"

urlpatterns = [
    # home
    path('', FluxView.as_view(), name='home'),

    # posts
    path('posts/', PostsView.as_view(), name='posts'),

    # ticket
    path('create-ticket/', TicketCreate.as_view(), name='create-ticket'),
    path('update-ticket/<int:pk>/', TicketUpdate.as_view(), name='update-ticket'),
    path('delete-ticket/<int:pk>/', TicketDelete.as_view(), name='delete-ticket'),

    # review
    path('delete-review/<int:pk>/', ReviewDelete.as_view(), name='delete-review'),
]
