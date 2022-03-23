from django.db import models, signals
from django.contrib.auth.models import User
from stdimage.models import StdImageField


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
    PlayerImg = StdImageField("Imagem", upload_to="Profile", variations={"thumb" : (124, 124)})
    From = models.CharField('From Where', max_length=120)
    PlayerName = models.CharField('Player Name', max_length=120)
    MsgBody = models.TextField('Mensagem', max_length=550)


class Usuario(Base):
    username = models.CharField("Username", max_length=120)
    email = models.EmailField("email")  
    password1 = models.CharField("password", max_length=120)  
    password2 = models.CharField("Confirm password", max_length=120) 


class MegaProfile(Usuario):
    UserImg = StdImageField("Imagem", upload_to="Profile", variations={"thumb" : (124, 124)})
    UserFrom = models.CharField('From Where', max_length=120)
    UserPlayerName = models.CharField('Player Name', max_length=120)
    UserMsgBody = models.TextField('Mensagem', max_length=550)


class FeedPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField("Data de criação", auto_now_add=True)
    MsgBody = models.TextField("Msg", max_length=550)
    Likes = models.ManyToManyField(User, related_name='FeedPost')

    def __str__(self):
        return str(self.author)

    @property
    def num_likes(self):
        return self.Likes.all().count()


class Comments(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField("Date", auto_now_add=True)
    Msg = models.CharField("comment", max_length=120)
    LikesComm = models.ManyToManyField(User, related_name='Comments')

    def __str__(self):
        return str(self.autor)

    @property
    def num_likes_comm(self):
        return self.LikesComm.all().count()
