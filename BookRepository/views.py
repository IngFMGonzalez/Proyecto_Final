from django.shortcuts import render
from django.http import HttpResponse
from BookRepository.models import Libro, Autor, Profile, Mensaje
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

###### INDEX ######

def index(request):
    context = {
        "libros": Libro.objects.all()
    }
    return render(request, "BookRepository/index.html", context)

###### ABOUT Me ######

def about(request):
    return render(request, "BookRepository/about_me.html")

###### LIBRO ######

class LibroCreate(LoginRequiredMixin, CreateView):
    model = Libro
    success_url = reverse_lazy("libro-list")
    fields = ['titulo','titulo','autor','prologo','genero','editorial','fecha_publicacion','imagen']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class LibroList(ListView):
    model = Libro

    def get_queryset(self):

        criterio = self.request.GET.get('criterio')

        if criterio:
            book = Libro.objects.filter(titulo__icontains=criterio)
        else:
            book = Libro.objects.all()

        return book
    
class LibroDetail(DetailView):
    model = Libro

class LibroUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Libro
    success_url = reverse_lazy("libro-list")
    fields = ['titulo','titulo','autor','prologo','genero','editorial','fecha_publicacion','imagen']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        libro_id = self.kwargs.get('pk')
        return Libro.objects.filter(publisher=user_id, id=libro_id).exists()

    def handle_no_permission(self):
        return render(self.request, "BookRepository/404_not_found.html")

class LibroDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy("libro-list")

    def test_func(self):
        user_id = self.request.user.id
        libro_id = self.kwargs.get('pk')
        return Libro.objects.filter(publisher=user_id, id=libro_id).exists()

    def handle_no_permission(self):
        return render(self.request, "BookRepository/404_not_found.html")



###### AUTOR ######

class AutorCreate(LoginRequiredMixin, CreateView):
    model = Autor
    success_url = reverse_lazy("autor-list")
    fields = ['nombre','apellido','nacionalidad','fecha_nacimiento','imagen']

    def form_valid(self, form):
        form.instance.publisher1 = self.request.user
        return super().form_valid(form)


class AutorList(ListView):
    model = Autor

    def get_queryset(self):

        criterio = self.request.GET.get('criterio')

        if criterio:
            book = Autor.objects.filter(nombre__icontains=criterio)
        else:
            book = Autor.objects.all()

        return book
    
class AutorDetail(DetailView):
    model = Autor

class AutorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Autor
    success_url = reverse_lazy("autor-list")
    fields = ['nombre','apellido','nacionalidad','fecha_nacimiento','imagen']

    def form_valid(self, form):
        form.instance.publisher1 = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        autor_id = self.kwargs.get('pk')
        return Autor.objects.filter(publisher1=user_id, id=autor_id).exists()

    def handle_no_permission(self):
        return render(self.request, "BookRepository/404_not_found.html")

class AutorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy("libro-list")

    def test_func(self):
        user_id = self.request.user.id
        autor_id = self.kwargs.get('pk')
        return Autor.objects.filter(publisher1=user_id, id=autor_id).exists()

    def handle_no_permission(self):
        return render(self.request, "BookRepository/404_not_found.html")



###### PERFIL ######

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy("index")
    

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['imagen']

    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(publisher2=user_id, id=profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "BookRepository/404_not_found.html")

class ProfileCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Profile
    template_name = 'BookRepository/profile_form.html'
    success_url = reverse_lazy('index')
    fields = ['imagen']

    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)
    
    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(publisher2=user_id, id=profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "BookRepository/404_not_found.html")



###### MENSAJERIA ######

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy("index")


class  MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()
    

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        return Mensaje.objects.filter(destinatario=user_id).exists()

