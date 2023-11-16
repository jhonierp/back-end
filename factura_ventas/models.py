from django.db import models

# Create your models here.
class Factura_Venta(models.Model):
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    cliente_f=models.ForeignKey('personas.Persona',on_delete=models.SET_NULL,null=True,blank=True)
    total_v=models.DecimalField(max_digits=10,decimal_places=2,null=True)  
    
    def __int__(self):
        return self.total_v