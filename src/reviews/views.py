# lib
from itertools import chain
# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# forms
from reviews.forms import CustomReviewForm, CustomTicketForm
# models
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
        context = super(PostsView, self).get_context_data(**kwargs)
        tickets = Ticket.objects.filter(user=self.request.user)
        reviews = Review.objects.filter(user=self.request.user)
        context['posts_list'] = list(sorted(chain(tickets, reviews),
                                            key=lambda post: post.time_created,
                                            reverse=True))
        return context


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = CustomTicketForm
    template_name = "reviews/ticket_create.html"


class TicketUpdate(LoginRequiredMixin, UpdateView):
    model = Ticket
    template_name = "reviews/ticket_update.html"
    fields = ["title", "description", "image", ]
    success_url = reverse_lazy("flux:posts")


class TicketDelete(LoginRequiredMixin, DeleteView):
    model = Ticket
    context_object_name = "post"
    success_url = reverse_lazy("flux:posts")


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    form_class = CustomReviewForm
    template_name = "reviews/review_create.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewCreate, self).get_context_data(**kwargs)
        context["ticket_form"] = CustomTicketForm
        return context

    def form_valid(self, form):
        if self.request.method == "POST":
            form_2 = CustomTicketForm(self.request.POST, self.request.FILES)
            if form_2.is_valid():
                ticket = form_2.save(commit=False)
                ticket.save()
                form.instance.ticket = ticket
        return super().form_valid(form)


class ReviewResponseCreate(LoginRequiredMixin, CreateView):
    model = Review
    form_class = CustomReviewForm
    template_name = "reviews/review_response_create.html"
    success_url = reverse_lazy("flux:home")

    def get_context_data(self, **kwargs):
        context = super(ReviewResponseCreate, self).get_context_data(**kwargs)
        ticket = get_object_or_404(Ticket, pk=self.kwargs["pk"])
        context["ticket"] = ticket
        return context

    def form_valid(self, form):
        ticket = get_object_or_404(Ticket, pk=self.kwargs["pk"])
        form.instance.ticket = ticket
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = "reviews/review_update.html"
    fields = ["headline", "rating", "body", ]
    success_url = reverse_lazy("flux:posts")

    def get_context_data(self, **kwargs):
        context = super(ReviewUpdate, self).get_context_data(**kwargs)
        ticket = get_object_or_404(Ticket, pk=self.kwargs["id_ticket"])
        context["ticket"] = ticket
        return context


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    context_object_name = "post"
    success_url = reverse_lazy("flux:posts")
