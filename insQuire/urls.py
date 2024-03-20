from django.urls import path
from django.utils.text import slugify
from insQuire import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'insQuire'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='all_categories'),
    path('categories/<slug:slugifiedName>/', views.category, name='category'),
    path('categories/question/<int:questionID>/', views.question, name='question'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('askquestion/', views.askQuestion, name='askQuestion'),
    path('answerquestion/<int:questionID>/', views.ansQuestion, name='answerQuestion'),
    path('answerquestionhtml/<int:questionID>/', views.ansQuestionhtml, name='answerQuestionhtml'),
    path('categories/question/upvote/', views.upvote1, name='upvote1'),
    path('categories/question/downvote/', views.downvote1, name='downvote1'),
    path('answerQuestion/', views.ansQuestion, name='answerQuestion'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)