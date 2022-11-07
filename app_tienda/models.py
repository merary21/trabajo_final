from django.db import models

# Create your models here.

class tblCiente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    Email = models.EmailField()
    
    def __str__(self):
        return self.nombre+ ''+self.apellido

class tblproducto(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)

class tblpedido(models.Model):
    cantidad = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
     
class tblTarjeta(models.Model):
    tipo = models.CharField(max_length=200)  
    Num_tarjeta = models.CharField(max_length=200)   
    def __str__(self):
        return self.Num_tarjeta
    
class tblpago(models.Model):
    Nombre_Cliente = models.ForeignKey(tblCiente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=5, decimal_places=2)
    Num_tarjeta = models.ForeignKey(tblTarjeta, on_delete=models.CASCADE) 
    Fecha = models.DateTimeField()
    
    
    
