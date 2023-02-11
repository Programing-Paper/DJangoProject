# Generated by Django 4.1.1 on 2023-02-10 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_empleado_cargoid'),
        ('novedades', '0010_remove_novedad_empleadoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.empleado', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='novedad',
            name='fecha',
            field=models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha registro'),
        ),
    ]