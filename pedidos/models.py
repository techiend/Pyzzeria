from django.db import models


class Tamano(models.Model):
    tamano_id = models.AutoField(primary_key=True)
    nombre_tamano = models.CharField(max_length=200)
    costo_tamano = models.DecimalField(max_digits=10, decimal_places=2)

    def get_name(self):
        return self.nombre_tamano

    def get_costo(self):
        return self.costo_tamano

    def __str__(self):
        return self.nombre_tamano + " | " + str(self.costo_tamano)

class Ingrediente(models.Model):
    ingrediente_id = models.AutoField(primary_key=True)
    nombre_ingrediente = models.CharField(max_length=200)
    costo_ingrediente = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_name(self):
        return self.nombre_ingrediente

    def get_costo(self):
        return self.costo_ingrediente
        
    def __str__(self):
        return self.nombre_ingrediente + " | " + str(self.costo_ingrediente)

class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField('Fecha pedido')
    nombre_cliente = models.CharField(max_length=200)
    def pizzas(self):
        return self.pizza_set.all()

    def costo_total(self):
        cont = 0
        for tot in self.pizza_set.all():
            cont = cont + tot.costo()
        return cont

    def __str__(self):
        return self.nombre_cliente
    
    def cant_pizzas(self):
        return len(self.pizza_set.all())

class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    tamano_id = models.ForeignKey(Tamano, on_delete=models.DO_NOTHING)
    
    def ingredientes(self):
        return self.pizza_ingrediente_set.all()

    def costo(self):
        cont = 0
        for ing in self.pizza_ingrediente_set.all().filter()[0:]:
            cont = cont + ing.ingrediente_id.get_costo()
        return cont + self.tamano_id.get_costo()

class Pizza_Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    pizza_id = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING, default=1)
    ingrediente_id = models.ForeignKey(Ingrediente, on_delete=models.DO_NOTHING, default=1)
