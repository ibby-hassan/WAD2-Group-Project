import json
from django.shortcuts import render
from insQuire.models import Category, Question, UserProfile
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from insQuire.forms import QuestionForm, AnswerForm, UserForm, UserProfileForm
from django.views.decorators.csrf import csrf_exempt

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
    context = {}
    next_url = '/'
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            
            # Saving the users details. Password has to be handled different as set_password hashes it, meaning it can't be used to authenticate after being saved.
            user = user_form.save(commit=False)
            plain_password = user_form.cleaned_data['password'] 
            user.set_password(plain_password)
            user.save()

            # Upon making the new account, logging the user in
            user = authenticate(username=user.username, password=plain_password)
            login(request, user)

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

            # Once registered and sign in, return back to the page they were on (given by the 'next' passed in from the register template, else redirect to '/' (index) page
            next_url = request.POST.get('next', '/')
            return redirect(next_url)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        next_url = request.GET.get('next', '/')
        
    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'next': next_url}
    return render(request, 'insQuire/register.html', context)


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
                return render(request, 'insQuire/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'insQuire/login.html', {'error_message': 'Invalid login details.'})
    else:
        return render(request, 'insQuire/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('insQuire:index'))

@login_required
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

@login_required
def ansQuestion(request, questionID):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():   
            question = Question.objects.get(id=questionID)
            categorySlugifiedName = question.category.slugifiedName
            user = request.user.userprofile
            answer = form.save(commit=False)
            answer.question = question
            answer.author = user
            answer.save()
            return redirect(reverse('insQuire:category', args=[categorySlugifiedName]))
    else:
        form = AnswerForm()
    return render(request, 'insQuire/answerQuestion.html', {'form': form})

@login_required
def ansQuestionhtml(request, questionID):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():   
            question = Question.objects.get(id=questionID)
            user = request.user.userprofile
            answer = form.save(commit=False)
            answer.question = question
            answer.author = user
            answer.save()
            return redirect(reverse('insQuire:question', args=[questionID]))
    else:
        form = AnswerForm()
    return render(request, 'insQuire/answerQuestion.html', {'form': form})



@csrf_exempt
def upvote1(request):
    if request.method == 'POST':
        quesID = json.loads(request.body)
        question = Question.objects.get(id=quesID['question_id'])
        question.votes += 1
        question.save()
        return JsonResponse({'votes': question.votes})
    
@csrf_exempt
def downvote1(request):
    if request.method == 'POST':
        quesID = json.loads(request.body)
        question = Question.objects.get(id=quesID['question_id'])
        question.votes -= 1
        question.save()
        return JsonResponse({'votes': question.votes})

def profile(request):
    user_profile = request.user.userprofile  # Retrieve the UserProfile instance for the current user
    user_posts = Question.objects.filter(author=user_profile)  # Filter questions by the user's UserProfile instance
    context = {
        'user_profile': user_profile,
        'user_posts': user_posts,
    }
    return render(request, 'insQuire/profile.html', context)


    
