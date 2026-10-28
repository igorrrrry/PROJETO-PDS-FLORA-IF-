
from django.shortcuts import render, get_object_or_404, redirect
from .models import Especie, FotoAluno


def home(request):
    return render(request, 'core/home.html')
def mapa(request):
    return render(request, 'mapa.html')
def curiosidades(request):
    return render(request, 'curiosidades.html')
def especie(request):
    return render(request, 'especie.html')
def sobre(request):
    return render (request, 'sobre.html')


def especies(request):
    especies = Especie.objects.all()

    return render(
        request,
        'especies.html',
        {
            'especies': especies
        }
    )


def detalhe_especie(request, slug):

    especie = get_object_or_404(
        Especie,
        slug=slug
    )

    if request.method == 'POST':

        foto = request.FILES.get('foto')

        nome_aluno = request.POST.get(
            'nome_aluno',
            ''
        )

        descricao = request.POST.get(
            'descricao',
            ''
        )

        if foto:
            FotoAluno.objects.create(
                especie=especie,
                foto=foto,
                nome_aluno=nome_aluno,
                descricao=descricao
            )

        return redirect(
            'detalhe_especie',
            slug=especie.slug
        )

    fotos = especie.fotos_alunos.filter(aprovada=True).order_by('-data_envio')

    return render(
        request,
        'detalhe_especie.html',
        {
            'especie': especie,
            'fotos': fotos
        }
    )
