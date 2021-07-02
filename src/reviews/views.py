# lib
from itertools import chain
# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Value, CharField
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# forms
from reviews.forms import CustomReviewForm, CustomTicketForm, CustomFollowForm
# models
from reviews.models import Ticket, Review, UserFollows


class FluxView(LoginRequiredMixin, ListView):
    """This class inherits from ListView for displaying the home page.

    Overload methods:
        get_context_data(self, **kwargs):
            Overload the get_context_data method for display all tickets and reviews
            related to the user connected in home page.
    """
    model = Ticket
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        """Overload the get_context_data method for display all tickets and reviews related to the user connected
        in home page."""
        context = super(FluxView, self).get_context_data(**kwargs)
        users_followed = UserFollows.objects.filter(followed_user=self.request.user)
        all_reviews = Review.objects.all()

        # Get the reviews in response to the user if they are not followed.
        # Reviews ID for followers_reviews
        follower_reviews_id = list(review.id for review in all_reviews if
                                   review.ticket.user == self.request.user
                                   and review.user != self.request.user
                                   and review.ticket.user not in list(
                                       user.user for user in users_followed))
        follower_reviews = Review.objects.filter(pk__in=follower_reviews_id)

        # Get all the tickets from the user and the people they follow.
        tickets = Ticket.objects.filter(
            user__in=list(chain(list(user.user for user in users_followed), [self.request.user])), his_review=False)

        # Get all the reviews from the user and the people they follow.
        reviews = Review.objects.filter(
            user__in=list(chain(list(user.user for user in users_followed),
                                [self.request.user]
                                )))

        follower_reviews_annotated = follower_reviews.annotate(content_type=Value('FOLLOWER_REVIEW', CharField()))
        tickets_annotated = tickets.annotate(content_type=Value('TICKET', CharField()))
        reviews_annotated = reviews.annotate(content_type=Value('REVIEW', CharField()))

        # I delete if there are duplicates reviews
        set_reviews = set(list(chain(reviews_annotated, follower_reviews_annotated)))

        context['flux_list'] = list(sorted(chain(tickets_annotated, set_reviews),
                                           key=lambda post: post.time_created,
                                           reverse=True))
        context['request'] = self.request
        return context


class PostsView(LoginRequiredMixin, ListView):
    """PostsView inherits from ListView for displaying the posts page.

    Overload methods:
        get_context_data(self, **kwargs):
            Overload the get_context_data method for display all tickets
             and reviews of to the user connected in posts page.
    """
    model = Ticket
    context_object_name = "my_posts"
    template_name = "reviews/posts.html"

    def get_context_data(self, **kwargs):
        """Overload the get_context_data method for display all tickets and reviews of to the user connected
        in posts page."""
        context = super(PostsView, self).get_context_data(**kwargs)
        tickets = Ticket.objects.filter(user=self.request.user)
        reviews = Review.objects.filter(user=self.request.user)
        context['posts_list'] = list(sorted(chain(tickets, reviews),
                                            key=lambda post: post.time_created,
                                            reverse=True))
        return context


class TicketCreateView(LoginRequiredMixin, CreateView):
    """TicketCreateView inherits from CreateView for creating ticket."""
    model = Ticket
    form_class = CustomTicketForm
    template_name = "reviews/ticket_create.html"

    def form_valid(self, form):
        """Overload the form_valid to add the user connected to the ticket."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    """TicketUpdateView inherits from UpdateView for updating ticket."""
    model = Ticket
    template_name = "reviews/ticket_update.html"
    fields = ["title", "description", "image", ]
    success_url = reverse_lazy("flux:posts")


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    """TicketDeleteView inherits from DeleteView for deleting ticket."""
    model = Ticket
    context_object_name = "post"
    success_url = reverse_lazy("flux:posts")


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """ReviewCreateView inherits from CreateView for creating review.

    Overload methods:
        get_context_data(self, **kwargs):
            Overload the get_context_data method to pass the CustomTicketForm in the context.
        form_valid(self, form):
            Overload the form_valid method to create the ticket related to the review
            and add it to the review.
    """
    model = Review
    form_class = CustomReviewForm
    template_name = "reviews/review_create.html"

    def get_context_data(self, **kwargs):
        """Overload the get_context_data method to pass the CustomTicketForm in the context."""
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context["ticket_form"] = CustomTicketForm
        return context

    def form_valid(self, form):
        """Overload the form_valid method to create the ticket related to the review
        and add it to the review.
        """
        # CustomTicketForm
        if self.request.method == "POST":
            form_2 = CustomTicketForm(self.request.POST, self.request.FILES)
            if form_2.is_valid():
                # Ticket
                ticket = form_2.save(commit=False)
                ticket.user = self.request.user
                ticket.his_review = True
                ticket.save()
                # Review
                form.instance.user = self.request.user
                form.instance.ticket = ticket
        return super().form_valid(form)


class ReviewResponseCreateView(LoginRequiredMixin, CreateView):
    """ReviewResponseCreateView inherits from CreateView for creating review.

    Overload methods:
        get_context_data(self, **kwargs):
            Overload the get_context_data method to pass the ticket in the context.
        form_valid(self, form):
            Overload the form_valid method to update the ticket related to the review
            and add it to the review.
    """
    model = Review
    form_class = CustomReviewForm
    template_name = "reviews/review_response_create.html"

    def get_context_data(self, **kwargs):
        """Overload the get_context_data method to pass the ticket in the context."""
        context = super(ReviewResponseCreateView, self).get_context_data(**kwargs)
        ticket = get_object_or_404(Ticket, pk=self.kwargs["pk"])
        context["ticket"] = ticket
        return context

    def form_valid(self, form):
        """Overload the form_valid method to update the ticket related to the review
        and add it to the review."""
        ticket = get_object_or_404(Ticket, pk=self.kwargs["pk"])
        # Ticket
        ticket.response = True
        ticket.save()
        # Review
        form.instance.ticket = ticket
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """ReviewUpdateView inherits from UpdateView for updating review.

    Overload methods:
        get_context_data(self, **kwargs):
            Overload the get_context_data method to pass the ticket in the context.
    """
    model = Review
    template_name = "reviews/review_update.html"
    fields = ["headline", "rating", "body", ]
    success_url = reverse_lazy("flux:posts")

    def get_context_data(self, **kwargs):
        """Overload the get_context_data method to pass the ticket in the context."""
        context = super(ReviewUpdateView, self).get_context_data(**kwargs)
        ticket = get_object_or_404(Ticket, pk=self.kwargs["id_ticket"])
        context["ticket"] = ticket
        return context


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """ReviewDeleteView inherits from DeleteView for deleting review."""
    model = Review
    context_object_name = "post"
    success_url = reverse_lazy("flux:posts")


class FollowCreateView(LoginRequiredMixin, CreateView):
    """FollowCreateView inherits from CreateView for creating follow.

    Overload methods:
        get_form_kwargs(self):
            Overload the get_form_kwargs method to pass the user connected in the form.
        get_context_data(self, **kwargs):
            Overload the get_context_data method to pass the follower et followed users.
        form_valid(self, form):
            Overload the form_valid method to update the ticket related to the review
            and add it to the review.
    """
    model = UserFollows
    form_class = CustomFollowForm
    template_name = "reviews/follow_create.html"

    def get_form_kwargs(self):
        """Overload the get_form_kwargs method to pass the user connected in the form."""
        kwargs = super(FollowCreateView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        """Overload the get_context_data method to pass the follower et followed users."""
        context = super(FollowCreateView, self).get_context_data(**kwargs)
        users_following = UserFollows.objects.filter(user=self.request.user)
        users_follower = UserFollows.objects.filter(followed_user=self.request.user)
        context["users_following"] = users_following
        context["users_follower"] = users_follower
        return context

    def form_valid(self, form):
        """Overload the form_valid to add the user connected to the followed_user."""
        form.instance.followed_user = self.request.user
        return super().form_valid(form)


class FollowDeleteView(LoginRequiredMixin, DeleteView):
    """ReviewDeleteView inherits from DeleteView for deleting review."""
    model = UserFollows
    context_object_name = "follow"
    success_url = reverse_lazy("flux:create-follow")
