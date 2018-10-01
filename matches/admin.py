from django.contrib import admin

from .models import Match


class MatchAdmin(admin.ModelAdmin):
    list_display = ('winner', 'loser', )
    list_filter = ('created_at', )


admin.site.register(Match, MatchAdmin)
