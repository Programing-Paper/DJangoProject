# Generated by Django 4.1.1 on 2023-04-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_remove_empleado_fecha_nacimiento'),
        ('activos', '0003_rename_idempleado_activo_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nombre_empleado', to='usuarios.empleado', verbose_name='Empleado'),
        ),
    ]