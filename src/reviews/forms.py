from django import forms

from reviews.models import Review, RATING_OPTIONS, Ticket


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
