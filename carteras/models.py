from django.db import models

# Create your models here.
class Cartera(models.Model):
    fecha_facturacion=models.DateTimeField(auto_now_add=True)
    fecha_vencimiento=models.DateField()
    pago=models.ForeignKey('pagos.Pago',on_delete=models.SET_NULL,null=True,blank=True) 
    
    def __int__(self):
        return self.pago