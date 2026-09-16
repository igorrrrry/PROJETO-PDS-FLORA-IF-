from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('arvore/',views.arvore, name='arvore'),
    path('mapa/', views.mapa, name='mapa'),
    ]
