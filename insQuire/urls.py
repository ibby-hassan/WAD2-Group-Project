from django.urls import path
from insQuire import views

app_name = 'insQuire'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='all_categories'),
    path('categories/<slug:slugifiedName>/', views.category, name='category'),
    path('categories/<slug:slugifiedName>/question/', views.question, name='question'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
]
