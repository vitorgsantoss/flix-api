from django.urls import path
from reviews import views


urlpatterns = [
    path('', views.ReviewListCreateView.as_view(), name='create_list_reviews'),
    path('<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_reviews'),
]
