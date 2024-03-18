from django.shortcuts import render
from insQuire.models import Category, Question
from django.db import models
from .forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from insQuire.forms import QuestionForm

def index(request):
    context = {}

    try:
        recent_questions = Question.objects.order_by('-dateAsked')[:10]
        popular_questions = Question.objects.order_by('-votes')[:10]
        context['recent_questions'] = recent_questions
        context['popular_questions'] = popular_questions
    except Question.DoesNotExist:
        context['recent_questions'] = None
        context['popular_questions'] = None

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
        context['question'] = question  

    except Question.DoesNotExist:
        context['question'] = None

    return render(request, 'insQuire/question.html', context)

def search(request):
    context = {}

    if request.method == 'POST':
        query = request.POST['search_bar']
        questions = Question.objects.filter(title__icontains=query)
        context['questions'] = questions
        context['query'] = query

    return render(request, 'insQuire/search.html', context)

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
    return redirect(reverse('insQuire:index'))

def askQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            user_profile = request.user.userprofile
            question.author = user_profile
            question.save()
            return redirect('insQuire:index')
    else:
        form = QuestionForm()
    categories = Category.objects.all()
    return render(request, 'insQuire/askQuestion.html', {'form': form, 'categories': categories})

def upvote(request, questionID):
    question = Question.objects.get(id=questionID)
    question.votes+=1
    question.save()
    return redirect("insQuire:category", slugifiedName = question.category.slugifiedName)

def upvoteindex(request, questionID):
    question = Question.objects.get(id=questionID)
    question.votes+=1
    question.save()
    return redirect("insQuire:index")

def downvote(request, questionID):
    question = Question.objects.get(id=questionID)
    question.votes-=1
    question.save()
    return redirect("insQuire:category", slugifiedName = question.category.slugifiedName)

def downvoteindex(request, questionID):
    question = Question.objects.get(id=questionID)
    question.votes-=1
    question.save()
    return redirect("insQuire:index")

def cantvote(request, questionID):
    return redirect("insQuire:login")
