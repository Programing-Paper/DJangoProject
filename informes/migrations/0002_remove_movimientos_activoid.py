# Generated by Django 4.1.1 on 2023-04-16 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientos',
            name='activoid',
        ),
    ]