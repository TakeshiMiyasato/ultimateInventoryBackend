# Generated by Django 4.0.6 on 2022-07-17 20:22

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructure', '0009_alter_venta_nit_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=django_fsm.FSMIntegerField(choices=[(0, 'Creado'), (1, 'Pagado'), (2, 'Pago Aceptado'), (3, 'Entregado'), (4, 'Pago Rechazado'), (5, 'Anulado')], default=0, protected=True),
        ),
    ]
