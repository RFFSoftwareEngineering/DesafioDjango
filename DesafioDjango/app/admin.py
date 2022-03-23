from django.contrib import admin
from .models import Base, User, Profile

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = ['criado', 'modificado', 'ativo']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['PlayerName', 'From']