from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Profile, MegaProfile
from .forms import ProfileModelForm, CustomUserCreationForm, MegaProfileModelForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


def home(request):
    if str(request.user) != "AnonymousUser":
        context = {
            "Perfil": Profile.objects.all()
         }
        return render(request, 'app/index.html', context)
    else:
        return redirect("UserProfile")


def cadastro(request):
    form1 = ProfileModelForm(request.POST, request.FILES) 
    if str(request.method) == "POST":
        if form1.is_valid():
            form1.save()
            messages.success(request, "Perfil Criado Com Sucesso!")
            form1 = ProfileModelForm()
        else:
            messages.error(request, "Erro ao Criar Perfil")
    else:
        form1 = ProfileModelForm()
    context = {
        "form1": form1
    }
    return render(request, 'app/cadastro.html', context)

def User_view(request):
    form2 = CustomUserCreationForm(request.POST or None)
    if str(request.method) == "POST":
        if form2.is_valid():
            form2.save()
            messages.success(request, "Usuário Criado Com Sucesso!")
            form2 = CustomUserCreationForm()
        else:
            messages.error(request, "Erro ao Criar Usuário")
    else:
        form2 = CustomUserCreationForm()
    context = {
        "form2": form2
    }
    return render(request, 'app/CriaUser.html', context)

def UserProfile(request):
    form3 = MegaProfileModelForm(request.POST, request.FILES)
    if str(request.method) == "POST":
        if form3.is_valid():
            form3.save()
            messages.success(request, "Usuário e Perfil Criado com Sucesso!")
            form3 = MegaProfileModelForm()
        else:
            messages.error(request, "Erro ao criar usuário e perfil")
    else:
        form3 = MegaProfileModelForm()
    context = {
        "form3": form3
    }
    return render(request, 'app/UserProfile.html', context)

def UserView(request):
    if str(request.user) != "AnonymousUser":
        context = {
            "User": MegaProfile.objects.all()
         }
        return render(request, 'app/UserView.html', context)
    else:
        return redirect("UserProfile")
