from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('player/<int:pk>/', views.player_detail, name='player_detail'),
    path('add/', views.add_player, name='add_player'),
    path('delete/<int:pk>/', views.delete_player, name='delete_player'),  # Удаление игрока
]
