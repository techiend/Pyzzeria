from django.contrib import admin
from .models import Pedido,Tamano,Ingrediente,Pizza,Pizza_Ingrediente

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Tamano)
admin.site.register(Ingrediente)
admin.site.register(Pizza)
admin.site.register(Pizza_Ingrediente)