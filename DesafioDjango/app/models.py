from django.db import models, signals
from django.contrib.auth.models import User
from stdimage.models import StdImageField


class MegaProfile(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    UserImg = StdImageField("Imagem", upload_to="Profile", variations={"thumb" : (124, 124)})
    UserFrom = models.CharField('From Where', max_length=120)
    UserPlayerName = models.CharField('Player Name', max_length=120)
    UserMsgBody = models.TextField('Mensagem', max_length=550)
    UserProfessionAt = models.CharField("Profession at", max_length=120, blank=True)

    def __str__(self):
        return str(self.UserPlayerName)


class FeedPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created = models.DateTimeField("Data de criação", auto_now_add=True)
    MsgBody = models.TextField("Msg", max_length=550)
    Likes = models.ManyToManyField(User, related_name='FeedPost', default=None, blank=True)

    def __str__(self):
        return str(self.MsgBody)

    @property
    def num_likes(self):
        return self.Likes.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class Comments(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateTimeField("Date", auto_now_add=True)
    Msg = models.CharField("comment", max_length=120)
    LikesComm = models.ManyToManyField(User, related_name='Comments', default=None, blank=True)

    def __str__(self):
        return str(self.autor)

    @property
    def num_likes_comm(self):
        return self.LikesComm.all().count()
