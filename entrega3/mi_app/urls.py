from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('mi_ruta/', views.mi_vista, name='nombre_de_la_vista'),
    path('home/', TemplateView.as_view(template_name='mi_app/base.html'), name='home'),
    path('crear_categoria/', TemplateView.as_view(template_name='mi_app/crear_categoria.html'), name='crear_categoria'),
    path('crear_producto/', TemplateView.as_view(template_name='mi_app/crear_producto.html'), name='crear_producto'),
    path('crear_cliente/', TemplateView.as_view(template_name='mi_app/crear_cliente.html'), name='crear_cliente'),
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),

]
