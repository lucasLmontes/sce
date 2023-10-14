from django.contrib import admin

from aplic.models import Administrador, Produto

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nomeAdmin', 'email')
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nomeProduto', 'valorProduto')
