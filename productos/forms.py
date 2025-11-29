from django import forms

from .models import Producto, Categoria, Etiqueta, DetallesProducto


class ProductoForm(forms.ModelForm):
    dimensiones = forms.CharField(required=False)
    peso = forms.DecimalField(
        required=False,
        decimal_places=2,
        max_digits=8,
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']

    def save(self, commit=True):
        producto = super().save(commit=False)
        dimensiones = self.cleaned_data.get('dimensiones')
        peso = self.cleaned_data.get('peso')

        if dimensiones or peso:
            if producto.detalles:
                producto.detalles.dimensiones = dimensiones
                producto.detalles.peso = peso
                producto.detalles.save()
            else:
                detalles = DetallesProducto.objects.create(
                    dimensiones=dimensiones or '',
                    peso=peso,
                )
                producto.detalles = detalles

        if commit:
            producto.save()
            self.save_m2m()
        return producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'etiquetas']
        widgets = {
            'etiquetas':forms.CheckboxSelectMultiple(),
        }


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
