"""Contains classes Ticket, Review and UsersFollows
which will allow us to handle relational databases of reviews app."""

# django
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

# settings.AUTH_USER_MODEL
CustomUserModel = get_user_model()


class Ticket(models.Model):
    """This is a class allowing to create a Ticket.
    Attributs:
        title = models.CharField(max_length=128, verbose_name="Titre")
        description = models.TextField(max_length=2048, blank=True)
        user = models.ForeignKey(to=CustomUserModel, on_delete=models.CASCADE)
        image = models.ImageField(null=True, blank=True, upload_to="images/")
        time_created = models.DateTimeField(auto_now_add=True)
        response = models.BooleanField(default=False)
        his_review = models.BooleanField(default=False)
    """
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=CustomUserModel, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    time_created = models.DateTimeField(auto_now_add=True)
    response = models.BooleanField(default=False)
    his_review = models.BooleanField(default=False)

    class Meta:
        """Meta options."""
        ordering = ["-time_created"]
        verbose_name = "Ticket"

    def __str__(self):
        """Represents the class objects as a string"""
        return str(self.title)

    @staticmethod
    def get_absolute_url():
        """Redirects to the home page after creating an Ticket instance."""
        return reverse("flux:home")


class Review(models.Model):
    """This is a class allowing to create a Review.
    Attributs:
        ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
        rating = models.PositiveSmallIntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(5)],
        )
        headline = models.CharField(max_length=128)
        body = models.TextField(max_length=8192, blank=True)
        user = models.ForeignKey(to=CustomUserModel, on_delete=models.CASCADE)
        time_created = models.DateTimeField(auto_now_add=True)
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(to=CustomUserModel, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options."""
        ordering = ["-time_created"]
        verbose_name = "Review"

    def __str__(self):
        """Represents the class objects as a string"""
        return str(self.headline)

    @staticmethod
    def get_absolute_url():
        """Redirects to the home page after creating an Review instance."""
        return reverse("flux:home")


class UserFollows(models.Model):
    """This is a class allowing to create a UserFollows.
    Attributs:
        user = models.ForeignKey(
        to=CustomUserModel, on_delete=models.CASCADE, related_name="following"
        )
        followed_user = models.ForeignKey(
            to=CustomUserModel, on_delete=models.CASCADE, related_name="followed_by"
        )
    """
    user = models.ForeignKey(
        to=CustomUserModel, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=CustomUserModel, on_delete=models.CASCADE, related_name="followed_by"
    )

    class Meta:
        """Meta options."""
        unique_together = ('user', 'followed_user',)
        verbose_name = "UserFollow"

    @staticmethod
    def get_absolute_url():
        """Redirects to the create-follow page after creating an UserFollows instance."""
        return reverse("flux:create-follow")
