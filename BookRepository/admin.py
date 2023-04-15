from django.contrib import admin
from BookRepository.models import Libro, Autor, Profile

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Profile)