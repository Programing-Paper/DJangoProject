# Generated by Django 4.1.1 on 2023-02-22 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_empleado_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='fecha',
            new_name='fecha_nacimiento',
        ),
    ]
