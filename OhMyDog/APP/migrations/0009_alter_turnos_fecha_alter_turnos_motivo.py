# Generated by Django 4.2.1 on 2023-05-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_alter_cliente_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='motivo',
            field=models.CharField(max_length=20),
        ),
    ]
