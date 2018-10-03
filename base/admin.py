from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import Player

admin.site.register(Player, UserAdmin)
