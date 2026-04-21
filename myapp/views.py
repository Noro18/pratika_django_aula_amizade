from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Estudante, Departamento
from .forms import EstudanteForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

@login_required(login_url="loginpage")
def home(request):
    return render(request, "home.html")

@login_required(login_url="loginpage")
def lista_estudante(request):
    # select_related hodi prevene N+1 queries
    return render(request, "lista_estudante.html", {"estudantes" : Estudante.objects.select_related("departamento").order_by("data_rejistu")}) 

@login_required(login_url="loginpage")
def add_estudante(request):
    if request.method  == "POST":
        form = EstudanteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista")
    return render(request, "add_estudante.html", {"form" : EstudanteForm()})

@login_required(login_url="loginpage")
def edit_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    if request.method == "POST":
        form = EstudanteForm(request.POST, request.FILES, instance=estudante)
        if form.is_valid():
            form.save()
            return redirect("lista")
    return render(request, "edit_estudante.html", {"form" : EstudanteForm(instance=estudante)})
        
@login_required(login_url="loginpage")
def delete_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    estudante.delete()
    return redirect("lista")

@login_required(login_url="loginpage")
def listadep(request):
    return render(request, "listadep.html", {"deps" : Departamento.objects.all()})

@login_required(login_url="loginpage")
def estudante_dep(request, id):
    dep = get_object_or_404(Departamento, id=id)
    estudante = Estudante.objects.filter(departamento= dep)
    return render(request, "estudante_dep.html", {"est_dep" : estudante, "dep" : dep})

@login_required(login_url="loginpage")
def konaba(request):
    return render(request, "konaba.html")

def loginpage(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username ka Password sei Sala !")
        else:
            messages.error(request, form.errors)
    return render(request, "login.html", {"form" : UserLoginForm()})

def logout_user(request):
    logout(request)
    return redirect("loginpage")