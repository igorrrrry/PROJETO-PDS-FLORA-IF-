from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Especie(models.Model):
    nome = models.CharField(max_length=150)
    nome_cientifico = models.CharField(max_length=150)
    origem = models.CharField(max_length=150)
    quantidade = models.PositiveIntegerField(default=0)

    foto = models.ImageField(
        upload_to='especies/',
        blank=True,
        null=True
    )

    descricao = models.TextField(blank=True)

    curiosidades = models.TextField(blank=True)

    utilidades = models.TextField(blank=True)

    slug = models.SlugField(
        unique=True,
        max_length=150
    )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'detalhe_especie',
            kwargs={'slug': self.slug}
        )


class FotoAluno(models.Model):
    especie = models.ForeignKey(
        Especie,
        on_delete=models.CASCADE,
        related_name='fotos_alunos'
    )

    foto = models.ImageField(
        upload_to='fotos_alunos/'
    )

    nome_aluno = models.CharField(
        max_length=100,
        blank=True
    )

    descricao = models.CharField(
        max_length=200,
        blank=True
    )

    data_envio = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.especie.nome} - {self.nome_aluno}'
