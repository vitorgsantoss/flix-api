from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('genres/', include('genres.urls')),
    path('admin/', admin.site.urls),
]
