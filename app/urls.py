from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/genres/', include('genres.urls')),
    path('api/v1/actors/', include('actors.urls')),
    path('admin/', admin.site.urls),
]
