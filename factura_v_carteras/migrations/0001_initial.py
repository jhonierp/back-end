# Generated by Django 4.2.2 on 2023-11-09 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factura_ventas', '0001_initial'),
        ('carteras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura_v_Cartera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carteras.cartera')),
                ('factura_venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura_ventas.factura_venta')),
            ],
        ),
    ]
