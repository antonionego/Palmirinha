from django.contrib import admin
from django.utils.html import mark_safe

from ReceitaApp.models import Categoria, Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    list_filter = ['categoria']

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Receita, ReceitaAdmin)

'''
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_display_links = ['nome', 'apelido']
    list_filter = ['data_nascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]
    filter_horizontal = ['interesses']
    

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)
'''