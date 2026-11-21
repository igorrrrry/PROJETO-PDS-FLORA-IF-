from django.shortcuts import render,redirect
from .models import Especie, FotoAluno

from django.utils.text import slugify
from django.contrib import messages
from .forms import EspecieForm

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

def admin(request):
    return render(request, "core/admin.html")

def listar_especies(request):

    especies = Especie.objects.all().order_by('nome')

    return render(request, 'core/gerenciamento(adm)/listar.html', {
        'especies': especies
    })

def cadastrar_especie(request):

    if request.method == 'POST':
        form = EspecieForm(request.POST, request.FILES)

        if form.is_valid():
            especie = form.save(commit=False)

            base_slug = slugify(especie.nome)
            slug = base_slug
            contador = 1

            while Especie.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{contador}'
                contador += 1

            especie.slug = slug
            especie.save()

            messages.success(request, 'Espécie cadastrada com sucesso!')
            return redirect('listar_especies')

    else:
        form = EspecieForm()

    return render(request, 'core/gerenciamento(adm)/cadastrar.html', {
        'form': form
    })

def editar_especie(request, id):

    especie = Especie.objects.filter(id=id).first()

    if especie is None:
        return redirect('listar_especies')

    if request.method == 'POST':
        form = EspecieForm(request.POST, request.FILES, instance=especie)

        if form.is_valid():
            form.save()

            messages.success(request, 'Espécie atualizada com sucesso!')
            return redirect('listar_especies')

    else:
        form = EspecieForm(instance=especie)

    return render(request, 'core/gerenciamento(adm)/editar.html', {
        'form': form,
        'especie': especie
    })

def excluir_especie(request, id):

    especie = Especie.objects.filter(id=id).first()
    if especie is None:
        return redirect('listar_especies')

    if request.method == 'POST':
        especie.delete()

        messages.success(request, 'Espécie excluída com sucesso!')
        return redirect('listar_especies')

    return render(request, 'core/gerenciamento(adm)/excluir.html', {
        'especie': especie
    })

def painel_admin(request):

    total_especies = Especie.objects.count()
    total_fotos = FotoAluno.objects.count()
    fotos_pendentes = FotoAluno.objects.filter(aprovada=False).count()
    return render(request, 'core/gerenciamento(adm)/inicial.html', {
        'total_especies': total_especies,
        'total_fotos': total_fotos,
        'fotos_pendentes': fotos_pendentes,})