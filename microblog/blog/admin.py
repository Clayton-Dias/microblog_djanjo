from django.contrib import admin

from .models import Postagem

# Register your models here.

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'imagem', 'conteudo', 'status', 'data_expiracao')
    search_fields = ('conteudo', 'data')
    list_filter=('data',)
