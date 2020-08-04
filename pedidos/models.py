from django.db import models


class Tamano(models.Model):
    tamano_id = models.IntegerField(primary_key=True)
    nombre_tamano = models.CharField(max_length=200)
    costo_tamano = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre_tamano

class Ingrediente(models.Model):
    ingrediente_id = models.IntegerField(primary_key=True)
    nombre_ingrediente = models.CharField(max_length=200)
    costo_ingrediente = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.nombre_ingrediente

class Pedido(models.Model):
    pedido_id = models.IntegerField(primary_key=True)
    fecha_pedido = models.DateField('Fecha pedido')
    nombre_cliente = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_cliente

class Pizza(models.Model):
    pizza_id = models.IntegerField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    tamano_id = models.ForeignKey(Tamano, on_delete=models.DO_NOTHING)

class Pizza_Ingrediente(models.Model):
    pizza_id = models.IntegerField(primary_key=True)
    ingrediente_id = models.ForeignKey(Ingrediente, on_delete=models.DO_NOTHING, default=0)
