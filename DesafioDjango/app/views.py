from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Profile
from .forms import ProfileModelForm
from django.contrib import messages


def home(request):
    context = {
        "Perfil": Profile.objects.all()
    }
    return render(request, 'app/index.html', context)


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

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
