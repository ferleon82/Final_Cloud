from rest_framework import viewsets
from .serializers import *
from .models import *

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

