
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('curiosidades/', views.curiosidades, name='curiosidades'),
    path('especie/', views.especie, name='especie'),
    path('sobre/', views.sobre, name='sobre'),
    path('especies/',views.especies,name='especies'),
    path('especies/<slug:slug>/',views.detalhe_especie,name='detalhe_especie'),

]
