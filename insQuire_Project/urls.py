from django.contrib import admin
from django.urls import path, include
from insQuire import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insQuire/', include('insQuire.urls')), # Maps all URLs starting with insQuire/ to the insQuire app
    path('admin/', admin.site.urls),
]
