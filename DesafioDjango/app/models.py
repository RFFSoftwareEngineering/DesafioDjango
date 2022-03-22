from django.db import models, signals
from django.contrib.auth.models import User

class Base(models.Model):
    criado = models.DateField("Data de criação", auto_now_add=True)
    modificado = models.DateField("Data de Atualização", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)


class User(Base):
    username = models.CharField("Username", max_length=120)
    email = models.EmailField("email")  
    password1 = models.CharField("password", max_length=120)  
    password2 = models.CharField("Confirm password", max_length=120)  

class Profile(Base):
    PlayerImg = models.ImageField(upload_to='media/')
    From = models.CharField('From Where', max_length=120)
    PlayerName = models.CharField('Player Name', max_length=120)
    MsgBody = models.TextField('Mensagem', max_length=550)