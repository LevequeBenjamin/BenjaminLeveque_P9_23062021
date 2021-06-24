from django.contrib import admin
from reviews.models import Ticket, Review


class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "image", "time_created",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("ticket", "rating", "headline", "time_created", "time_created",)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
