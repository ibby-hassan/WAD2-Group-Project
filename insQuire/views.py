from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'insQuire/index.html', context)

def categories(request):
    context = {}
    return render(request, 'insQuire/categories.html', context)