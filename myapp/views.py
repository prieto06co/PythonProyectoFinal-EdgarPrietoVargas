from symtable import Class

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Componente, Colaborador, Sede, Perfil_Usuario
from .forms import ComponenteFormulario, SedeFormulario, ColaboradorFormulario, EditarUsuario, UsuarioPerfilForumlario
# Create your views here.

@login_required()
def vista_perfil_usuario(request):
    return render(request,"myapp/perfil-usuario.html")

@login_required()
def cambiar_clave_usuario(request):

    if request.method == "POST":
        form= PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
        else:
            return redirect("inicio")
    else:
        form = PasswordChangeForm(request.user)

    return render(request,"myapp/forms/cambiar-clave-usuario.html", {"form":form})

@login_required()
def vista_editar_perfil(request):

    perfil, _ =Perfil_Usuario.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form= EditarUsuario(request.POST, instance=request.user)
        perfil_form=UsuarioPerfilForumlario(request.POST, request.FILES, instance=perfil)
        if form.is_valid() and perfil_form.is_valid():
            form.save()
            perfil_form.save()
            return redirect("perfil-usuario")
        else:
            return redirect("inicio")
    else:
        form = EditarUsuario(instance=request.user)
        perfil_form=UsuarioPerfilForumlario(instance=perfil)
    return render(request,"myapp/forms/editar-perfil.html", {"form":form, "perfil_form":perfil_form})


def vista_registro(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = UserCreationForm()
    return render(request,"myapp/forms/registro.html", {"form":form})


def vista_logueo(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("inicio")
        else:
            return redirect("logueo")
            
    else:
        return render(request,"myapp/forms/logueo.html")

def vista_deslogueo(request):
    logout(request)
    return redirect("logueo")

def inicio(request):
    return render(request,"myapp/index.html")

def acerca_de_nosotros(request):
    return render(request,"myapp/acerca-de-nosotros.html")

class ComponenteListView(ListView):
    model = Componente
    context_object_name = "componentes"
    template_name = "myapp/componentes.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Componente.objects.filter(nombre__icontains=query)
        return Componente.objects.all()

# def componentes(request):
#     query = request.GET.get("q")
#     if query:
#         componentes = Componente.objects.filter(nombre__icontains=query)
#     else:
#         componentes = Componente.objects.all()
#     return render(request, "myapp/componentes.html", {"componentes": componentes})


class ColaboradorListView(LoginRequiredMixin, ListView):
    model = Colaborador
    context_object_name = "colaboradores"
    template_name = "myapp/colaboradores.html"

    # Redirige a la página de login si el usuario no está autenticado
    login_url = 'logueo'  # Ajusta la URL según tu configuración
    redirect_field_name = 'next'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Colaborador.objects.filter(
                Q(nombre__icontains=query) | Q(apellido__icontains=query)
            )
        return Colaborador.objects.all()

class SedeListView(ListView):
    model = Sede
    context_object_name = "sedes"
    template_name = "myapp/sedes.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Sede.objects.filter(nombre__icontains=query)
        return Sede.objects.all()

# def formulario_componentes_api(request):
#     if request.method == "POST":
#         componente_form = ComponenteFormulario(request.POST)
#
#         if componente_form.is_valid():
#             info_limpia = componente_form.cleaned_data
#             componente = Componente(nombre=info_limpia["nombre"], cantidad=info_limpia["cantidad"])
#             componente.save()
#             return redirect("componentes")
#     else:
#         componente_form = ComponenteFormulario()
#
#     contexto = {"form": componente_form}
#
#     return render(request, "myapp/forms/componente-formulario.html", contexto)

class ComponenteCreateView(LoginRequiredMixin,CreateView):
    model = Componente
    template_name = "myapp/forms/componente-formulario.html"
    login_url = 'logueo'
    redirect_field_name = 'next'
    #fields = "__all__" #No funciona en conjunto con form_class
    form_class = ComponenteFormulario  # Aquí se especifica el formulario personalizado
    success_url = reverse_lazy("componentes")

class SedeCreateView(LoginRequiredMixin,CreateView):
    model = Sede
    template_name = "myapp/forms/sede-formulario.html"
    login_url = 'logueo'
    redirect_field_name = 'next'
    form_class = SedeFormulario
    success_url = reverse_lazy("sedes")

class ColaboradorCreateView(LoginRequiredMixin,CreateView):
    model = Colaborador
    template_name = "myapp/forms/colaborador-formulario.html"
    login_url = 'logueo'  # Ajusta la URL según tu configuración
    redirect_field_name = 'next'
    form_class = ColaboradorFormulario
    success_url = reverse_lazy("colaboradores")

class ComponenteDeleteView(DeleteView):
    model = Componente
    template_name = "myapp/deletes/componente-eliminar.html"
    success_url = reverse_lazy("componentes")

class SedeDeleteView(DeleteView):
    model = Sede
    template_name = "myapp/deletes/sede-eliminar.html"
    success_url = reverse_lazy("sedes")

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = "myapp/deletes/colaborador-eliminar.html"
    success_url = reverse_lazy("colaboradores")


class ComponenteUpdateView(UpdateView):
    model = Componente
    template_name = "myapp/updates/componente-editar.html"
    fields = "__all__"
    success_url = reverse_lazy("componentes")

class SedeUpdateView(UpdateView):
    model = Sede
    template_name = "myapp/updates/sede-editar.html"
    fields = "__all__"
    success_url = reverse_lazy("sedes")

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    template_name = "myapp/updates/colaborador-editar.html"
    fields = "__all__"
    success_url = reverse_lazy("colaboradores")

class ComponenteDetailView(DetailView):
    model = Componente
    template_name = "myapp/componente-detalle.html"

class ColaboradorDetailView(DetailView):
    model = Colaborador
    template_name = "myapp/colaborador-detalle.html"

class SedeDetailView(DetailView):
    model = Sede
    template_name = "myapp/sede-detalle.html"