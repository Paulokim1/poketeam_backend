from django.urls import path

from . import views

urlpatterns = [
    path('api/pokemon/<int:note_id>/', views.api_pokemon), 
    path('api/pokemon/', views.api_pokemon_list)
]