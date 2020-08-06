from django.urls import path
from . import views
app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pedido_id>/', views.detail, name='detail'),
    path('lista/', views.lista, name='lista'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('pizza/', views.pizza, name='pizza'),
    path('administracion/', views.admin, name='administracion'),
    path('administracion/detalle/<int:pedido_id>/', views.admin_detalle, name='detalle'),
    path('administracion/ingrediente/', views.venta_ingrediente, name='venta_ingrediente'),
    
]