# Generated by Django 3.1.2 on 2020-10-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20201029_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='protocol',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
