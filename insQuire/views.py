from django.shortcuts import render
from insQuire.models import Category, Question
from django.db import models
from .forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    if "s" in request.GET:
        search = request.GET["s"]
        questions = Question.objects.filter(title__icontains=search)
        return render(request, 'insQuire/question.html', {'questions': questions})
    context = {}

    try:
        context['Recent Questions'] = Question.objects.order_by('-dateAsked')[:10]
        context['Popular Questions'] = Question.objects.order_by('-votes')[:10]
    except Question.DoesNotExist:
        context['Recent Questions'] = None
        context['Popular Questions'] = None
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

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                    'insQuire/register.html',
    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('insQuire:index'))
            else:
                return HttpResponse("Your insQuire account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'insQuire/login.html')


def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
# Take the user back to the homepage.
    return redirect(reverse('insQuire:index'))
