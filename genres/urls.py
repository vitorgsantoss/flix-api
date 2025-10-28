from django.urls import path
from genres import views

app_name = 'genres'

urlpatterns = [
    path('', views.ListCreateView.as_view(), name='create_list_genres'),
    path('<int:pk>/', views.RetrieveUpdateDestroyView.as_view(), name='detail_update_genre'),
]
