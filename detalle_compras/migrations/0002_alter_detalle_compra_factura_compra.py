# Generated by Django 4.2.2 on 2023-11-09 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura_compras', '0001_initial'),
        ('detalle_compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_compra',
            name='factura_compra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura_compras.factura_compra'),
        ),
    ]
