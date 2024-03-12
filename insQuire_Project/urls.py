from django.contrib import admin
from django.urls import path, include
from insQuire import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='index'),
    path('insQuire/', include('insQuire.urls')), # Maps all URLs starting with insQuire/ to the insQuire app
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
