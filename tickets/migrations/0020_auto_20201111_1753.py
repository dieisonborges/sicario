# Generated by Django 3.1.3 on 2020-11-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0019_auto_20201110_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='deadline',
            field=models.DateTimeField(verbose_name='Prazo'),
        ),
    ]
