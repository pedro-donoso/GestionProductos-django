from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class DetallesProducto(models.Model):
    dimensiones = models.CharField(max_length=100, blank=True)
    peso = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Detalles {self.id}"


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos',
    )
    etiquetas = models.ManyToManyField(
        Etiqueta,
        blank=True,
        related_name='productos',
    )
    detalles = models.OneToOneField(
        DetallesProducto,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='producto',
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

