# Generated by Django 4.0.6 on 2022-07-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructure', '0008_rename_fechalastupdate_stock_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='nit_factura',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]