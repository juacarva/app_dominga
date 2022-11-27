from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=120)
    rut = models.CharField(max_length=12, unique = True)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nombre

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo_ext = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)
    proveedor = models.ManyToManyField(Proveedor)
    #imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    #Nota: en related_name se agrega el nombre con el que identificaremos desde Productos (la entidad relacionada) a  todas
    #las imágenes
