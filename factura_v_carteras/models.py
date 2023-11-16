from django.db import models

# Create your models here.
class Factura_v_Cartera(models.Model):
    factura_venta=models.ForeignKey('factura_ventas.Factura_Venta',on_delete=models.SET_NULL,null=True,blank=True)
    cartera=models.ForeignKey('carteras.Cartera',on_delete=models.SET_NULL,null=True,blank=True)

    #def __int__(self):
      #  return self.producto_venta