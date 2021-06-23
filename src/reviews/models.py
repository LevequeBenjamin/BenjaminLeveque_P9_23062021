from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify

# settings.AUTH_USER_MODEL
CustomUser = get_user_model()


class Ticket(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    time_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_created"]
        verbose_name = "Ticket"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now=True)


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="followed_by"
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)
