
from django.urls import path
from . import views

urlpatterns = [
    # Páginas públicas
    path('', views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('curiosidades/', views.curiosidades, name='curiosidades'),
    path('especie/', views.especie, name='especie'),
    path('sobre/', views.sobre, name='sobre'),
    path('detalhe_especies/<slug:slug>/',views.detalhe_especie,name='detalhe_especie'),
    path('adm/fotos/',views.gerenciar_fotos,name='gerenciar_fotos'),
    path('adm/fotos/aprovar/<int:id>/',views.aprovar_foto,name='aprovar_foto'),
    path('adm/fotos/rejeitar/<int:id>/',views.rejeitar_foto,name='rejeitar_foto'),
]
