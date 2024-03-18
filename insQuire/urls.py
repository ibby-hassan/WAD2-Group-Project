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
    path('categories/question/upvote/<int:questionID>/', views.upvote, name='upvote'),
    path('categories/question/downvote/<int:questionID>/', views.downvote, name='downvote'),
    path('categories/question/upvoteindex/<int:questionID>/', views.upvoteindex, name='upvoteindex'),
    path('categories/question/downvoteindex/<int:questionID>/', views.downvoteindex, name='downvoteindex'),
    path('categories/question/cantvote/<int:questionID>/', views.cantvote, name='cantvote')


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)