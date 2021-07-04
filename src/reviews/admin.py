from django.contrib import admin
from reviews.models import Ticket, Review, UserFollows


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "image", "time_created", "response", "his_review",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "user", "rating", "headline", "time_created",)


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "followed_user",)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
