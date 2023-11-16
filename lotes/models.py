from django.db import models

# Create your models here.

class Lote(models.Model):
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    numero_lote = models.PositiveIntegerField(null=True)
    producto_lote=models.ForeignKey('productos.Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cantidad=models.DecimalField(max_digits=10,decimal_places=2,null=True)  
    
    def __str__(self):
        if self.producto_lote:
            return f"Lote {self.numero_lote} - {self.producto_lote.nombre}"
        else:
            return f"Lote {self.numero_lote} - Sin producto asociado"