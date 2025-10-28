from django.urls import path
from actors import views

app_name = 'actors'

urlpatterns = [
    path('', views.ListCreateView.as_view(), name='create_list_actors'),
    path('<int:pk>/', views.RetrieveUpdateDestroyView.as_view(), name='detail_update_actors'),
]