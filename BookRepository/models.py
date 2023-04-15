from django.db import models
from django.contrib.auth.models import User

###### LIBRO ######

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    prologo = models.TextField(max_length=500)
    genero = models.CharField(max_length=50)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="libros")
    creacion = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.id} - Titulo: {self.titulo} - Autor: {self.autor} - Genero: {self.genero} - Editorial: {self.editorial}"


###### AUTOR ######

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad =models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    publisher1 = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher1")
    imagen = models.ImageField(upload_to="autores")

    def __str__(self):
        return f"{self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Nacionalidad: {self.nacionalidad} - Fecha de Nacimiento: {self.fecha_nacimiento}"
    

###### PERFIL ######

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    imagen = models.ImageField(upload_to="profiles")


###### MENSAJERIA ######

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")