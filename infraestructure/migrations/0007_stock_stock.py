# Generated by Django 4.0.6 on 2022-07-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructure', '0006_delete_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
