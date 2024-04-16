
from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from django.http import HttpResponse

def mi_vista(request):
    if request.method == 'POST':
        return HttpResponse('El formulario fue enviado por POST')
    else:
        return HttpResponse('Método no permitido')



def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'mi_app/crear_categoria.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/crear_producto.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_cliente')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/crear_cliente.html', {'form': form})

def buscar_producto(request):
    # Lógica para obtener los productos (por ejemplo, consultando la base de datos)
    productos = Producto.objects.all()  # Obtén todos los productos

    # Renderiza la plantilla con el contexto de productos
    return render(request, 'mi_app/buscar_producto.html', {'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_app/lista_productos.html', {'productos': productos})