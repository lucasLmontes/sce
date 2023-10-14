from django.db import models
from stdimage.models import StdImageField
import uuid
from django.utils.translation import gettext_lazy as _

class Administrador(models.Model):
    nomeAdmin = models.CharField(_('Nome'), max_length=100)
    idAdmin = models.AutoField(_('Id'), primary_key=True)
    email = models.EmailField(_('Email'), blank=True, max_length=100)

    def __str__(self):
        return self.nomeAdmin

class Produto(models.Model):
    nomeProduto = models.CharField(_('Nome do produto'), max_length=200)
    idProduto = models.AutoField(_('Id'), primary_key=True)
    valorProduto = models.DecimalField(_('Valor do produto'), max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')
