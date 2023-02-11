# Generated by Django 4.1.1 on 2023-02-10 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_empleado_cargoid'),
        ('configuracion', '0006_remove_admin_empleadoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='empleadoid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.empleado', verbose_name='Empleado'),
        ),
    ]
