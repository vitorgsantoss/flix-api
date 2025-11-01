from django.urls import path
from actors import views


urlpatterns = [
    path('', views.ActorListCreateView.as_view(), name='create_list_actors'),
    path('<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_actors'),
]
