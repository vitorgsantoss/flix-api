from django.urls import path
from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewListCreateView.as_view(), name='create_list_reviews'),
    path('<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='detail_update_reviews'),
]
