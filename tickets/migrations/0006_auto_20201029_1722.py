# Generated by Django 3.1.2 on 2020-10-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20201029_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='protocol',
            field=models.CharField(default='1Y2YOY4YEY9', max_length=10),
        ),
    ]
