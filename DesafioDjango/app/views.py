from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import MegaProfile, FeedPost, Like, Comments
from .forms import CustomUserCreationForm, MegaProfileModelForm, FeedPostModelForm, CommentsModelForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def home(request):
    form6 = FeedPostModelForm(request.POST or None)
    user = request.user
    if str(request.user) != "AnonymousUser":
        if str(request.method) == "POST":
            if form6.is_valid():
                form6.save()
                messages.success(request, "Post feito com Sucesso!")
                form6 = FeedPostModelForm()
            else:
                messages.error(request, "Erro ao postar")
        else:
            form6 = FeedPostModelForm()
        data = MegaProfile.objects.all()
        paginator = Paginator(data, 1)
        page_number = request.GET.get('home')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'form6': form6
         }
        return render(request, 'app/index.html', context)
    else:
        return redirect("CreateUser")


def User_view(request):
    form2 = CustomUserCreationForm(request.POST or None)
    if str(request.method) == "POST":
        if form2.is_valid():
            form2.save()
            messages.success(request, "Usuário Criado Com Sucesso!")
            form2 = CustomUserCreationForm()
        else:
            messages.error(request, "Erro ao Criar Usuário")
        return redirect('login')
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
        return redirect('home')
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
        return redirect("CreateUser")

def post_on_feed(request):
    form4 = FeedPostModelForm(request.POST or None)
    user = request.user
    if str(request.method) == "POST":
        if form4.is_valid():
            form4.save()
            messages.success(request, "Post feito com Sucesso!")
            form4 = FeedPostModelForm()
        else:
            messages.error(request, "Erro ao postar")
    else:
        form4 = FeedPostModelForm()
    context = {
        "form4": form4,
        "Posts": FeedPost.objects.all(),
        "Comms": Comments.objects.all(),
        "user": user
    }
    return render(request, 'app/FeedPost.html', context)

def like_post(request):
    user = request.user    
    if str(request.method) == "POST":
        post_id = request.POST.get('post_id')
        post_obj = FeedPost.objects.get(id=post_id)

        if user in post_obj.Likes.all():
            post_obj.Likes.remove(user)
        else:
            post_obj.Likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'UnLike'
            else:
                like.value = 'Like'

        like.save()
        post_id2 = request.POST.get('post_id')
        post_obj2 = Comments.objects.get(id=post_id)

        if user in post_obj2.LikesComm.all():
            post_obj2.LikesComm.remove(user)
        else:
            post_obj2.LikesComm.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'UnLike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('FeedPost')

def comm_post(request):
    form5 = CommentsModelForm(request.POST or None)
    user = request.user
    if str(request.method) == "POST":
        if form5.is_valid():
            form5.save()
            messages.success(request, "Comentário feito com Sucesso!")
            form5 = CommentsModelForm()
        else:
            messages.error(request, "Erro ao postar comment")
        return redirect('FeedPost')
    else:
        form4 = CommentsModelForm()
    context = {
        "form5": form5,
        "user": user
    }
    return render(request, 'app/CommPost.html', context)