from django.contrib import admin

from .models import Match


class MatchAdmin(admin.ModelAdmin):
    fields = ('winner', 'loser', )
    list_display = ('created_at', 'winner', 'loser', )
    list_filter = ('created_at', )


admin.site.register(Match, MatchAdmin)
