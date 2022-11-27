from django.contrib import admin
from .models import *

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ImagenProductoAdmin,
    ]


# Register your models here.
admin.site.register(Proveedor)
admin.site.register(CategoriaProducto)
admin.site.register(Producto, ProductoAdmin)


#Configurar el título del panel admin
admin.site.site_header = "Panel Administración | Accesorios Dominga"
admin.site.site_title = "Panel Administración | Accesorios Dominga"
admin.site.index_title = "Accesorios Dominga"