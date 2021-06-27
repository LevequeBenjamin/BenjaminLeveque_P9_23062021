from django.urls import path
from reviews.views import FluxView, TicketCreate, TicketUpdate, PostsView, TicketDelete, ReviewDelete, \
    ReviewUpdate, ReviewCreate, ReviewResponseCreate

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
    path('create-review/', ReviewCreate.as_view(), name='create-review'),
    path('create-review/<int:pk>/', ReviewResponseCreate.as_view(), name='create-response-review'),
    path('update-review/<int:pk>/', ReviewUpdate.as_view(), name='update-review'),
    path('delete-review/<int:pk>/', ReviewDelete.as_view(), name='delete-review'),
]
