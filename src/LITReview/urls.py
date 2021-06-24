from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flux/', include('reviews.urls'))
    #path('compte/login', include('django.contrib.auth.urls')),
]
