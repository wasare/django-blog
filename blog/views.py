from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Olá Django - index')
    # return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request):
    # return HttpResponse('Olá django')
    return render(request, 'home.html')