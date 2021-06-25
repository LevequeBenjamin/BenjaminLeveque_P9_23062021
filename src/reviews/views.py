from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from reviews.models import Ticket, Review


class FluxView(LoginRequiredMixin, ListView):
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
        return context


class PostsView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = "my_posts"
    template_name = "reviews/posts.html"

    def get_context_data(self, **kwargs):
        ticket_btn_hide = []
        context = super(PostsView, self).get_context_data(**kwargs)
        tickets = Ticket.objects.filter(user=self.request.user)
        reviews = Review.objects.filter(user=self.request.user)
        context['posts_list'] = list(sorted(chain(tickets, reviews),
                                            key=lambda post: post.time_created,
                                            reverse=True))
        for review in reviews:
            if self.request.user == review.user:
                ticket_btn_hide.append(review.ticket.id)
        context['ticket_btn_hide'] = ticket_btn_hide
        context['request'] = self.request
        return context


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "reviews/ticket_create.html"
    fields = ["title", "description", "image", ]


class TicketUpdate(LoginRequiredMixin, UpdateView):
    model = Ticket
    template_name = "reviews/ticket_update.html"
    fields = ["title", "description", "image", ]


class TicketDelete(LoginRequiredMixin, DeleteView):
    model = Ticket
    context_object_name = "post"
    success_url = reverse_lazy("flux:posts")


# class ReviewCreate(LoginRequiredMixin, CreateView):
#     model = Review
#     template_name = "reviews/review_create.html"
#     fields = ["title", "description", "image", ]
#
#
# class ReviewUpdate(LoginRequiredMixin, UpdateView):
#     model = Review
#     template_name = "reviews/review_update.html"
#     fields = ["title", "description", "image", ]
#
#
class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    context_object_name = "post"
    success_url = reverse_lazy("flux:home")
