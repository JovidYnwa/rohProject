from django.contrib import admin
from . import models


@admin.register(models.AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name', 'join_date')
    list_display_links = ('email',)

@admin.register(models.AuthSocialLink)
class AuthSocialLink(admin.ModelAdmin):
    list_display = ('user', 'link')
