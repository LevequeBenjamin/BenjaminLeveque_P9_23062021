# django
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# settings.AUTH_USER_MODEL
from django.urls import reverse

CustomUserModel = get_user_model()

RATING_OPTIONS = {
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
}


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=CustomUserModel, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    time_created = models.DateTimeField(auto_now=True)
    response = models.BooleanField(default=False)
    his_review = models.BooleanField(default=False)

    class Meta:
        ordering = ["-time_created"]
        verbose_name = "Ticket"

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse("flux:home")


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(to=CustomUserModel, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]
        verbose_name = "Review"

    def __str__(self):
        return self.headline

    @staticmethod
    def get_absolute_url():
        return reverse("flux:posts")


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=CustomUserModel, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=CustomUserModel, on_delete=models.CASCADE, related_name="followed_by"
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)
        verbose_name = "UserFollow"
