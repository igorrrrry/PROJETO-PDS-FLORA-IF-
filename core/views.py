from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def arvore(request):
    return render(request, 'arvore.html')
def mapa(request):
    return render(request, 'mapa.html')