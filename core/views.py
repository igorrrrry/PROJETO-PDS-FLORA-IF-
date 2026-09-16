from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def arvore(request):
    return render(request, 'arvore.html')
def mapa(request):
    return render(request, 'mapa.html')