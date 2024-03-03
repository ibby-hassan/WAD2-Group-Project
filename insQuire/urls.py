from django.urls import path
from insQuire import views

app_name = 'insQuire'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='all_categories'),
    path('categories/<slug:slugifiedName>/', views.category, name='category'),
    path('question/<int:questionID>/', views.question, name='question'),
]