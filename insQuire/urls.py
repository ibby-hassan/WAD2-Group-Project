from django.urls import path
from insQuire import views

app_name = 'insQuire'

urlpatterns = [
    path('', views.index, name='index'),
]