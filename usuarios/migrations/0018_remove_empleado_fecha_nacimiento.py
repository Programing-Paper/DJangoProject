# Generated by Django 4.1.1 on 2023-03-01 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_empleado_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_nacimiento',
        ),
    ]