from .models import Produto, Categoria, Compra
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView

################################
# categoria classes
################################
class CategoriasList(ListAPIView):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerizalizer

################################
# produtos classes
################################
class ProdutosList(ListAPIView):
  queryset = Produto.objects.all()
  serializer_class = ProdutoDetalheSerizalizer

class ProdutosRetrieve(RetrieveAPIView):
  queryset = Produto.objects.all()
  serializer_class = ProdutoDetalheSerizalizer

class ProdutosCreate(CreateAPIView):
  permission_classes = [IsAdminUser]
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerizalizer

class ProdutosUpdate(UpdateAPIView):
  permission_classes = [IsAdminUser]
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerizalizer


################################
# produtos classes
################################
class ComprasCreate(CreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Compra.objects.all()
  serializer_class = CompraSerizalizer

class ComprasList(ListAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Compra.objects.all()
  serializer_class = CompraDetalheSerizalizer

  def get_queryset(self):
    usuario = self.request.user
    if usuario.is_superuser:
      return Compra.objects.all()
    return Compra.objects.filter(usuario=usuario)

class ComprasRetrieve(RetrieveAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Compra.objects.all()
  serializer_class = CompraDetalheSerizalizer

  def get_queryset(self):
    usuario = self.request.user
    if usuario.is_superuser:
      return Compra.objects.all()
    return Compra.objects.filter(usuario=usuario)
