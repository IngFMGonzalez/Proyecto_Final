"""BookRepository_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BookRepository.views import  index, about, LibroCreate, LibroList, LibroDelete, LibroDetail, LibroUpdate, AutorList, AutorCreate, AutorDetail, AutorUpdate, AutorDelete, SignUp, Login, Logout, ProfileUpdate, ProfileCreate, MensajeCreate, MensajeDelete, MensajeList

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('libro/list', LibroList.as_view(), name="libro-list"),
    path('libro/create', LibroCreate.as_view(), name="libro-create"),
    path('libro/<pk>/detail', LibroDetail.as_view(), name="libro-detail"),
    path('libro/<pk>/update', LibroUpdate.as_view(), name="libro-update"),
    path('libro/<pk>/delete', LibroDelete.as_view(), name="libro-delete"),
    path('autor/list', AutorList.as_view(), name="autor-list"),
    path('autor/create', AutorCreate.as_view(), name="autor-create"),
    path('autor/<pk>/detail', AutorDetail.as_view(), name="autor-detail"),
    path('autor/<pk>/update', AutorUpdate.as_view(), name="autor-update"),
    path('autor/<pk>/delete', AutorDelete.as_view(), name="autor-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('about_me', about, name="about_me"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)