from django.urls import path
from . import views

urlpatterns = [
    path('', views.concepto_gastos),
    path('new/', views.crear_concepto_gastos, name="nuevo_concepto"),
    path('eliminar_concepto/<int:concepto_id>/', views.eliminar_concepto_gasto, name="eliminar_concepto"),
    path('modificar_concepto/<int:concepto_id>/', views.modificar_concepto, name='modificar_concepto')

    
]
