# Generated by Django 4.2.2 on 2023-11-09 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detalle_ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_venta',
            old_name='precio_unitario',
            new_name='precio_producto',
        ),
    ]
