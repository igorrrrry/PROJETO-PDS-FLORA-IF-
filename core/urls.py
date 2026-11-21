
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
    path('adm/', views.painel_admin, name='adm'),
    path('adm/especies/listar',views.listar_especies,name='listar_especies'),
    path('adm/especies/cadastrar/',views.cadastrar_especie,name='cadastrar_especie'),
    path('adm/especies/editar/<int:id>/',views.editar_especie,name='editar_especie'),
    path('adm/especies/excluir/<int:id>/',views.excluir_especie,name='excluir_especie'),
]
