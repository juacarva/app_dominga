from django.shortcuts import render, get_object_or_404
from .models import Producto, ImagenProducto

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'app/home.html', {'productos': productos})

def detalle(request, id):
    producto = Producto.objects.get(id=id)
    imagenes = ImagenProducto.objects.all().filter(producto_id = id)
    data = {
        'producto': producto,
        'imagenes': imagenes,
    }
    return render(request, 'app/detalle.html', data)