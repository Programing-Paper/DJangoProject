# Generated by Django 4.1.1 on 2023-01-26 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=25)),
                ('so', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=10)),
                ('fecha', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha registro')),
                ('observaciones', models.CharField(max_length=200)),
                ('estado', models.CharField(default='Asignado', max_length=20)),
                ('empleadoid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.empleado', verbose_name='Empleadoid')),
            ],
        ),
    ]
