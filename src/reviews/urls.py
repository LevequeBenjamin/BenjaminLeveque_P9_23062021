from django.urls import path
from reviews.views import FluxView, TicketCreateView, TicketUpdateView, PostsView, TicketDeleteView, ReviewDeleteView, \
    ReviewUpdateView, ReviewCreateView, ReviewResponseCreateView, FollowCreateView, FollowDeleteView

app_name = "flux"

urlpatterns = [
    # home
    path('', FluxView.as_view(), name='home'),

    # posts
    path('posts/', PostsView.as_view(), name='posts'),

    # ticket
    path('ticket/', TicketCreateView.as_view(), name='create-ticket'),
    path('ticket/<int:pk>/edit/', TicketUpdateView.as_view(), name='update-ticket'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='delete-ticket'),

    # review
    path('review/', ReviewCreateView.as_view(), name='create-review'),
    path('review/<int:pk>/', ReviewResponseCreateView.as_view(), name='create-response-review'),
    path('review/<int:pk>/<int:id_ticket>/edit/', ReviewUpdateView.as_view(), name='update-review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),

    # follows
    path('follows/', FollowCreateView.as_view(), name='create-follow'),
    path('follow/<int:pk>/delete/', FollowDeleteView.as_view(), name='delete-follow'),
]
