from django import forms
from .models import Especie


class EspecieForm(forms.ModelForm):

    class Meta:
        model = Especie

        fields = [
            'nome',
            'nome_cientifico',
            'origem',
            'quantidade',
            'foto',
            'descricao',
            'curiosidades',
            'utilidades',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome popular da espécie'
            }),

            'nome_cientifico': forms.TextInput(attrs={
                'placeholder': 'Nome científico'
            }),

            'origem': forms.TextInput(attrs={
                'placeholder': 'Ex: Nativa do Brasil'
            }),

            'quantidade': forms.NumberInput(attrs={
                'min': 0
            }),

            'descricao': forms.Textarea(attrs={
                'rows': 4
            }),

            'curiosidades': forms.Textarea(attrs={
                'rows': 4
            }),

            'utilidades': forms.Textarea(attrs={
                'rows': 4
            }),
        }
