from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flux/', include('reviews.urls')),
    #path('signup/', include('accounts.urls')),
]
