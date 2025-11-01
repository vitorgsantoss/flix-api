from django.urls import path
from movies import views


urlpatterns = [
    path('', views.MovieListCreateView.as_view(), name='create_list_movies'),
    path('<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_movies'),
    path('stats/', views.MovieStatsView.as_view(), name='stats_movies'),
]
