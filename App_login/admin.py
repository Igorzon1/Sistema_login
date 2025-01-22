from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'cargo', 'is_active', 'is_staff')  # Exibe essas informações na lista
    search_fields = ('cpf', 'cargo')  # Adiciona a funcionalidade de pesquisa
    list_filter = ('cargo', 'is_active', 'is_staff')  # Filtros para facilitar a busca no admin

# Registra o modelo Usuario no admin
admin.site.register(Usuario, UsuarioAdmin)

