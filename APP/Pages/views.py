from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def help(request):
    return render(request, 'help.html')

def calculadora(request):
    return render(request, 'calculadora.html')

def londrina(request):
    return render(request, 'londrina.html')