from django.db import models

# Create your models here.
medio_pago = (
    ("Efectivo", "Efectivo"),
    ("Tarjeta de Crédito", "Tarjeta de Crédito"),
    ("Transferencia Bancaria", "Transferencia Bancaria"),
)
estado_pago = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
)
class Pago(models.Model):
    medio_pago=models.CharField(max_length=255,choices=medio_pago)
    estado_pago=models.CharField(max_length=255,choices=estado_pago)
    factura_v=models.ForeignKey('factura_ventas.Factura_Venta',on_delete=models.SET_NULL,null=True,blank=True)
    factura_c=models.ForeignKey('factura_compras.Factura_Compra',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.estado_pago
    
    