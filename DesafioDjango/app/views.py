from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Profile


def home(request):
    context = {
        "Perfil": Profile.objects.all()
    }
    return render(request, 'app/index.html', context)


def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

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
