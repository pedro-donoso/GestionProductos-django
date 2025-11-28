from django.contrib import admin

from .models import Producto, Categoria, Etiqueta, DetallesProducto

@admin.register(Producto)


class ProductoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'precio', 'categoria', 'creado_en')
    list_filter = ('categoria', 'etiquetas')
    search_fields = ('nombre', 'descripcion')
    admin.site.register(Categoria)
    admin.site.register(Etiqueta)
    admin.site.register(DetallesProducto)
