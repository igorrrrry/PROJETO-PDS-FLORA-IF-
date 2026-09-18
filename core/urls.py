from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('arvore/',views.arvore, name='arvore'),
    path('mapa/', views.mapa, name='mapa'),
    path('curiosidades/', views.curiosidades, name='curiosidades'),
    path('especie/', views.especie, name='especie'),
    path('especiecatalogos/', views.especiecatalogos, name='especiecatalogos'),
    path('sobre/', views.sobre, name='sobre'),
    
    ]
