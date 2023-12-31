# Generated by Django 4.2.2 on 2023-11-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('total_c', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('proveedor_f', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.persona')),
            ],
        ),
    ]
