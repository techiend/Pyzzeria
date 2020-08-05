from django.urls import path
from . import views
app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pedido_id>/', views.detail, name='detail'),
    path('lista/', views.lista, name='lista'),
    path('solicitud/', views.solicitud, name='solicitud'),
    path('administracion/', views.admin, name='administracion'),
    path('administracion/detalle/<int:pedido_id>/', views.admin_detalle, name='detalle'),
]