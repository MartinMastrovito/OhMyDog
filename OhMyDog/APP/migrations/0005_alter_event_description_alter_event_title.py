# Generated by Django 4.1.7 on 2023-07-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_contactoadop_dueño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
