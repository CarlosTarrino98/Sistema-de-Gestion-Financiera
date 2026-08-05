from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ingresos/', views.lista_ingresos, name='lista_ingresos'),
    path('gastos/', views.lista_gastos, name='lista_gastos'),
    path('añadir/ingreso/', views.añadir_ingreso, name='añadir_ingreso'),
    path('añadir/gasto/', views.añadir_gasto, name='añadir_gasto'),
    path('editar/ingreso/<int:pk>/', views.editar_ingreso, name='editar_ingreso'),
    path('editar/gasto/<int:pk>/', views.editar_gasto, name='editar_gasto'),
    path('eliminar/ingreso/<int:pk>/', views.eliminar_ingreso, name='eliminar_ingreso'),
    path('eliminar/gasto/<int:pk>/', views.eliminar_gasto, name='eliminar_gasto'),
    path('eliminar/ingresos/', views.eliminar_ingresos, name='eliminar_ingresos'),
    path('eliminar/gastos/', views.eliminar_gastos, name='eliminar_gastos'),
    path('seguimiento/', views.generar_seguimiento, name='generar_seguimiento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)