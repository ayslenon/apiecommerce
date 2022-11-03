from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
  nomeCategoria = models.CharField(max_length=30)

  def __str__(self):
    return self.nomeCategoria

class Produto(models.Model):
  nomeProduto = models.CharField(max_length=50)
  descricaoProduto = models.CharField(max_length=250)
  precoProduto = models.FloatField()
  imagemProduto = models.URLField()
  categoriaProduto = models.ForeignKey(Categoria, on_delete=models.PROTECT)

  def __str__(self):
    return self.nomeProduto

class Compra(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.PROTECT)
  precoTotal = models.FloatField(null=True)
  data = models.DateTimeField(auto_now_add=True)
  descricaoCompra = models.CharField(max_length=250)

  def __str__(self):
    return self.descricaoCompra

class ItemCompra(models.Model):
  idCompra = models.ForeignKey(Compra, on_delete=models.PROTECT, related_name='itens')
  produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
  quantidade = models.IntegerField()
  subTotal = models.FloatField(null=True)

  def __str__(self):
    return self.produto

