from django.urls import path
from reviews.views import FluxView, TicketCreate, TicketUpdate, PostsView, TicketDelete, ReviewDelete, \
    ReviewUpdate, ReviewCreate, ReviewResponseCreate, FollowCreate

app_name = "flux"

urlpatterns = [
    # home
    path('', FluxView.as_view(), name='home'),

    # posts
    path('posts/', PostsView.as_view(), name='posts'),

    # ticket
    path('ticket/', TicketCreate.as_view(), name='create-ticket'),
    path('ticket/<int:pk>/edit/', TicketUpdate.as_view(), name='update-ticket'),
    path('ticket/<int:pk>/delete/', TicketDelete.as_view(), name='delete-ticket'),

    # review
    path('review/', ReviewCreate.as_view(), name='create-review'),
    path('review/<int:pk>/', ReviewResponseCreate.as_view(), name='create-response-review'),
    path('review/<int:pk>/<int:id_ticket>/edit/', ReviewUpdate.as_view(), name='update-review'),
    path('review/<int:pk>/delete/', ReviewDelete.as_view(), name='delete-review'),

    # follows
    path('follow/', FollowCreate.as_view(), name='create-follow'),
]
