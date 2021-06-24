from itertools import chain

from django.views.generic import ListView

from reviews.models import Ticket, Review


class FluxView(ListView):
    model = Ticket
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review
        return context
