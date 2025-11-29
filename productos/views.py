from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.db.models import Q, Count

from django.db import connection

from .models import Producto, Categoria, Etiqueta

from .forms import ProductoForm, CategoriaForm, EtiquetaForm


@login_required

def index(request):
    context = {
        'total_productos': Producto.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_etiquetas': Etiqueta.objects.count(),
    }
    return render(request, 'index.html', context)


@login_required

def lista_productos(request):
    q = request.GET.get('q', '')
    productos = Producto.objects.all()

    if q:
        productos = productos.filter(
            Q(nombre__icontains=q) | Q(descripcion__icontains=q)
        )

    productos_caros = productos.filter(precio__gt=10000)   # filter()
    productos_baratos = productos.exclude(precio__gt=10000)  # exclude()

    context = {
        'productos': productos,
        'query': q,
        'productos_caros': productos_caros.count(),
        'productos_baratos': productos_baratos.count(),
    }
    return render(request, 'productos/lista.html', context)


@login_required

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear.html', {'form': form})


@login_required

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    # Ejemplo raw()
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT p.nombre, p.precio, c.nombre
            FROM productos_producto p
            JOIN productos_categoria c ON p.categoria_id = c.id
            WHERE p.id = %s
            """,
            [id],
        )
        raw_data = cursor.fetchone()

    return render(
        request,
        'productos/detalle.html',
        {'producto': producto, 'raw_data': raw_data},
    )


@login_required

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    initial = {}
    if producto.detalles:
        initial['dimensiones'] = producto.detalles.dimensiones
        initial['peso'] = producto.detalles.peso

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto, initial=initial)

    return render(
        request,
        'productos/editar.html',
        {'form': form, 'producto': producto},
    )


@login_required

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('lista_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})


# Categorías
@login_required

def lista_categorias(request):
    categorias = Categoria.objects.annotate(total_productos=Count('productos'))
    return render(request, 'categorias/lista.html', {'categorias': categorias})


@login_required

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/formulario.html', {'form': form})


@login_required

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/formulario.html', {'form': form})


@login_required

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias/eliminar.html', {'categoria': categoria})


# Etiquetas
@login_required

def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.annotate(total_productos=Count('productos'))
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})


@login_required

def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'etiquetas/formulario.html', {'form': form})


@login_required

def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiquetas/formulario.html', {'form': form})


@login_required

def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'etiquetas/eliminar.html', {'etiqueta': etiqueta})


@login_required

def perfil(request):
    return render(request, 'perfil.html')
