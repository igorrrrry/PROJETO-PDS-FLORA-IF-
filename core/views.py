from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST

from .models import Especie, FotoAluno
from .forms import EspecieForm
def administrador(user):
    return user.is_authenticated and user.is_staff

def home(request):
    return render(request, 'core/home.html')

def mapa(request):
    return render(request, 'core/mapa.html')

def curiosidades(request):
    return render(request, 'core/curiosidades.html')

def especie(request):
    especies = Especie.objects.all()
    return render(request, 'core/especie.html', {'especies': especies})

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


@user_passes_test(administrador, login_url='/admin/login/')
def gerenciar_fotos(request):

    fotos = FotoAluno.objects.select_related(
        'especie'
    ).order_by('-data_envio')

    return render(
        request,
        'core/gerenciamento(adm)/fotos_alunos.html',
        {
            'fotos': fotos
        }
    )


@user_passes_test(administrador, login_url='/admin/login/')
@require_POST
def aprovar_foto(request, id):

    foto = FotoAluno.objects.filter(id=id).first()

    if foto is None:
        messages.error(request, 'Foto não encontrada!')
        return redirect('gerenciar_fotos')

    foto.aprovada = True
    foto.save()

    messages.success(request, 'Foto aprovada com sucesso!')

    return redirect('gerenciar_fotos')


@user_passes_test(administrador, login_url='/admin/login/')
@require_POST
def rejeitar_foto(request, id):

    foto = FotoAluno.objects.filter(id=id).first()

    if foto is None:
        messages.error(request, 'Foto não encontrada!')
        return redirect('gerenciar_fotos')

    if foto.foto:
        foto.foto.delete(save=False)

    foto.delete()

    messages.success(request, 'Foto rejeitada com sucesso!')

    return redirect('gerenciar_fotos')
