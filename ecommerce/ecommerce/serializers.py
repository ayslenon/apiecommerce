from rest_framework.serializers import ModelSerializer, CharField
from .models import Produto, Compra, ItemCompra, Categoria
from django.contrib.auth.models import User

from rest_framework import serializers
######################################################
# classes para implementação de modelos curtos (saidas)
class UsuarioSerizalizer(ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

class ProdutoDetalheSerizalizer(ModelSerializer):
  categoriaProduto = CharField(source='categoriaProduto.nomeCategoria')
  class Meta:
    model = Produto
    fields = "__all__"

class ItemCompraDetalheSerizalizer(ModelSerializer):
  produto = ProdutoDetalheSerizalizer()
  class Meta:
    model = ItemCompra
    fields = "__all__"

class CompraDetalheSerizalizer(ModelSerializer):
  usuario = UsuarioSerizalizer()
  itens = ItemCompraDetalheSerizalizer(many=True)
  class Meta:
    model = Compra
    fields = "__all__"
    depth = 1


###########################################################
# classes para criação de elementos
class CategoriaSerizalizer(ModelSerializer):
  class Meta:
    model = Categoria
    fields = "__all__"

class ProdutoSerizalizer(ModelSerializer):
  class Meta:
    model = Produto
    fields = "__all__"

class ItemCompraSerizalizer(ModelSerializer):
  class Meta:
    model = ItemCompra
    fields = ['produto', 'quantidade']
  
class CompraSerizalizer(ModelSerializer):
  itens = ItemCompraSerizalizer(many=True)
  usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Compra
    fields = ('usuario', 'precoTotal', 'descricaoCompra', 'itens')

  def create(self, validated_data):
    itens = validated_data.pop('itens')
    precoTotal = 0
    # for i in itens:
     
    #   sub = i.quantidade * prod.precoProduto
    #   i['subTotal'] = sub
    #   precoTotal += sub
    validated_data.update({'precoTotal':precoTotal})
    compra = Compra.objects.create(**validated_data)
    for item in itens:
      ItemCompra.objects.create(idCompra = compra, **item)
    compra.save()
    return compra