from django.contrib import admin

from .models import Ad


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'condition',)
    search_fields = ('title',)


admin.site.register(Ad, AdAdmin)
