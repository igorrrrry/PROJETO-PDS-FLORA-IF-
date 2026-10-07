from django.contrib import admin
from .models import Especie, FotoAluno


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'nome_cientifico',
        'origem',
        'quantidade'
    )

    prepopulated_fields = {
        'slug': ('nome',)
    }


@admin.register(FotoAluno)
class FotoAlunoAdmin(admin.ModelAdmin):
    list_display = (
        'especie',
        'nome_aluno',
        'data_envio'
    )
