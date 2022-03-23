from django.contrib import admin
from .models import Base, User, Usuario, Profile, MegaProfile, FeedPost, Comments, Like, Comments

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = ['criado', 'modificado', 'ativo']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['PlayerName', 'From']

@admin.register(Usuario)
class UsuaroAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password1', 'password2']

@admin.register(MegaProfile)
class MegaProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password1', 'password2', 'UserImg', 'UserFrom', 'UserPlayerName', 'UserMsgBody']

@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    list_display = ['author', 'num_likes', 'created', 'MsgBody']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['autor', 'num_likes_comm', 'criado', 'Msg']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'value']
