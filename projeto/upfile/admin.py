from django.contrib import admin
from .models import User, Arquivo

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'arquivo')
    list_filter = ('nome','extensao')
    list_per_page = 10
    search_fields = ('nome', 'extensao')
    
admin.site.register(User)
admin.site.register(Arquivo, ArquivoAdmin)