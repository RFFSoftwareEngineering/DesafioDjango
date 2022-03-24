from django.contrib import admin
from .models import MegaProfile, FeedPost, Comments, Like

@admin.register(MegaProfile)
class MegaProfileAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'UserImg', 'UserFrom', 'UserPlayerName', 'UserMsgBody']

@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    list_display = ['author', 'num_likes', 'created', 'MsgBody']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['autor', 'num_likes_comm', 'criado', 'Msg']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'value']
