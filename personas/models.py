from django.db import models

# Create your models here.
tipo_persona = [
        ('cliente', 'Cliente'),
        ('proveedor', 'Proveedor')
    ]
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    correo = models.CharField(max_length=150,null=True)
    tipo_persona=models.CharField(max_length=255,choices=tipo_persona,null=True)
    
    def __str__(self):
        return self.nombre
