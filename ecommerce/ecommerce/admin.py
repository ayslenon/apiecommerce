from django.contrib import admin
from .models import Categoria, Compra, ItemCompra, Produto

# 
@admin.register(Categoria, Compra, ItemCompra, Produto)
class EcommerceAdmin(admin.ModelAdmin):
  pass