from django.urls import path
from genres import views


urlpatterns = [
    path('', views.GenreListCreateView.as_view(), name='create_list_genres'),
    path('<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_genres'),
]
