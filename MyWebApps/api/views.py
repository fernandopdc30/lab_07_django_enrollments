from rest_framework import viewsets
from MyWebApps.models import Producto
from MyWebApps.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer