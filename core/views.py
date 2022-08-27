from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Marca, Categoria
from core.serializers import MarcaSerializer, CategoriaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
