# Generated by Django 4.1.1 on 2023-02-22 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_empleado_fecha_nacimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='fecha_nacimiento',
            new_name='fecha',
        ),
    ]