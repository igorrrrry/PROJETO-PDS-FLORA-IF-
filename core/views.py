from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
def arvore(request):
    return render(request, 'arvore.html')
def mapa(request):
    return render(request, 'mapa.html')
def curiosidades(request):
    return render(request, 'curiosidades.html')
def especie(request):
    return render(request, 'especie.html')
def especiecatalogos(request):
    return render(request, 'especiescatalogos.html')
def sobre(request):
    return render (request, 'sobre.html')
