
from django.shortcuts import render,redirect
from .models import Especie, FotoAluno


def home(request):
    return render(request, 'core/home.html')
def mapa(request):
    return render(request, 'core/mapa.html')
def curiosidades(request):
    return render(request, 'core/curiosidades.html')
def especie(request):
    return render(request, 'core/especie.html')
def sobre(request):
    return render (request, 'core/sobre.html')

def detalhe_especie(request, slug):

    especie = Especie.objects.get(slug=slug)

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
        return redirect('detalhe_especie',slug=especie.slug)

    fotos = especie.fotos_alunos.filter(aprovada=True).order_by('-data_envio')

    return render(request,'core/detalhe_especie.html',{'especie': especie,'fotos': fotos}
)
