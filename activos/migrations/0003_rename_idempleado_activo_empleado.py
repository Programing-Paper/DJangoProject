# Generated by Django 4.1.1 on 2023-03-14 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0002_alter_activo_idactivo_alter_activo_situacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activo',
            old_name='idempleado',
            new_name='empleado',
        ),
    ]