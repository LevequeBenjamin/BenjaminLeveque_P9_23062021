from itertools import chain

from django.views.generic import ListView, DetailView

from reviews.models import Ticket, Review


class FluxView(ListView):
    model = Ticket
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        ticket_btn_hide = []
        context = super(FluxView, self).get_context_data(**kwargs)
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()
        context['flux_list'] = list(sorted(chain(tickets, reviews),
                                           key=lambda post: post.time_created,
                                           reverse=True))
        for review in reviews:
            if self.request.user == review.user:
                ticket_btn_hide.append(review.ticket.id)
        context['ticket_btn_hide'] = ticket_btn_hide
        context['request'] = self.request
        print(context)
        return context
