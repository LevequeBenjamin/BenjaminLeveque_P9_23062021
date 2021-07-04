"""Contains the forms of reviews app."""

# django
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

# models
from accounts.models import CustomUser
from reviews.models import Review, Ticket, UserFollows

# RadioSelect options
RATING_OPTIONS = [
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
]


class CustomTicketForm(forms.ModelForm):
    """CustomTicketForm inherits from ModelForm for creating ticket form."""

    class Meta:
        """Meta options."""
        model = Ticket
        fields = ["title", "description", "image", ]


class CustomReviewForm(forms.ModelForm):
    """CustomReviewForm inherits from ModelForm for creating review form."""
    rating = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=RATING_OPTIONS,
                               )

    class Meta:
        """Meta options."""
        model = Review
        fields = ["headline", "rating", "body", ]


class CustomFollowForm(forms.ModelForm):
    """CustomFollowForm inherits from ModelForm for creating follow form.

    Overload methods:
        clean_user:(self):
            Overload the clean_user method to validate the inputs.
    """

    def __init__(self, *args, **kwargs):
        """Inits connected user."""
        self.request_user = kwargs.pop(
            'request_user')

        super(CustomFollowForm, self).__init__(*args, **kwargs)

    user = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"})
    )

    class Meta:
        """Meta options."""
        model = UserFollows
        fields = ["user", ]

    def clean_user(self):
        """Overload the clean_user method to validate the inputs."""
        username = self.cleaned_data.get("user", None)
        users = CustomUser.objects.all()
        users_follower = UserFollows.objects.filter(followed_user=self.request_user)
        if username == str(self.request_user):
            raise ValidationError("Vous ne pouvez pas vous follow")
        elif username not in [user.username for user in users]:
            raise ValidationError("Cet utilisateur n'existe pas")
        if username in [user.user.username for user in users_follower]:
            raise ValidationError("Cet utilisateur est déjà follow")
        else:
            user = get_object_or_404(CustomUser, username=username)
        return user
