# Generated by Django 4.1.1 on 2023-02-10 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0011_novedad_empleado_alter_novedad_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='fecha',
            field=models.DateField(auto_now_add=True, help_text='MM/DD/AAAA', verbose_name='Fecha registro'),
        ),
    ]
