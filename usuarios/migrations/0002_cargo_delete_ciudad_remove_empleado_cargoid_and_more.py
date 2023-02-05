# Generated by Django 4.1.1 on 2023-02-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomcargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Sueldo')),
            ],
        ),
        migrations.DeleteModel(
            name='Ciudad',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='cargoid',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='ciudadid',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='idempleado',
        ),
        migrations.AddField(
            model_name='empleado',
            name='compania',
            field=models.CharField(choices=[('medellin', 'Medellin'), ('bogota', 'Bogota'), ('cucuta', 'Cucuta'), ('cartagena', 'Cartagena'), ('bucaramanga', 'Bucaramanga'), ('otro', 'Otro')], default='otro', max_length=30, verbose_name='Compañia'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='documento',
            field=models.CharField(default='null', max_length=20, primary_key=True, serialize=False, verbose_name='Documento de Identidad'),
        ),
    ]