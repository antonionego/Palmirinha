from django.contrib import admin
from django.utils.html import mark_safe

from ReceitaApp.models import Categoria, Receita

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Receita)
