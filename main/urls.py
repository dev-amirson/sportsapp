from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:pk>/update/', views.team_update, name='team_update'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),
    path('team/<int:team_id>/assign-players/', views.assign_players_to_team, name='assign_players_to_team'),
    path('players/', views.player_list, name='player_list'),
    path('players/<int:pk>/', views.player_detail, name='player_detail'),
    path('players/create/', views.player_create, name='player_create'),
    path('players/<int:pk>/update/', views.player_update, name='player_update'),
    path('players/<int:pk>/delete/', views.player_delete, name='player_delete'),
    path('accounts/register/', views.register, name='register'),
]
