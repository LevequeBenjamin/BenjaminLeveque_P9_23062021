from django import forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect

from accounts.models import CustomUser
from reviews.models import Review, RATING_OPTIONS, Ticket, UserFollows


class CustomTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image", ]


class CustomReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_OPTIONS,
                               widget=forms.RadioSelect
                               )

    class Meta:
        model = Review
        fields = ["headline", "rating", "body", ]


class FollowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop(
            'request_user')

        super(FollowForm, self).__init__(*args, **kwargs)

    user = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"})
    )

    class Meta:
        model = UserFollows
        fields = ["user", ]

    def clean_user(self):
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
