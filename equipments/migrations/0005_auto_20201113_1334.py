# Generated by Django 3.1.3 on 2020-11-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0004_auto_20201113_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(choices=[('1', 'Operacional'), ('2', 'Inoperante Parcialmente'), ('3', 'Inoperante Total')], default=1, max_length=1, verbose_name='Situação'),
        ),
    ]