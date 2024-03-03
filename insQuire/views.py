from django.shortcuts import render
from insQuire.models import Category, Question
from django.db import models

def index(request):
    context = {}
    return render(request, 'insQuire/index.html', context)

def categories(request):
    context = {}

    try:
        categories = Category.objects.all()
        context['categories'] = categories

    except Category.DoesNotExist:
        context['categories'] = None

    return render(request, 'insQuire/categories.html', context)

def category(request, slugifiedName):
    context = {}

    try:
        category = Category.objects.get(slugifiedName=slugifiedName)
        questions = Question.objects.filter(category=category)
        context['category'] = category
        context['questions'] = questions

    except Category.DoesNotExist:
        context['category'] = None
        context['questions'] = None

    return render(request, 'insQuire/category.html', context)

def question(request, questionID):
    context = {}

    try:
        question = Question.objects.get(id=questionID)
        context['questions'] = question

    except Question.DoesNotExist:
        context['questions'] = None

    return render(request, 'insQuire/question.html', context)
