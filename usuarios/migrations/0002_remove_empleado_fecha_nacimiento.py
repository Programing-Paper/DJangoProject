# Generated by Django 4.1.1 on 2023-02-22 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_nacimiento',
        ),
    ]