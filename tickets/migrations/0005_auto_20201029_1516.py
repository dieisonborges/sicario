# Generated by Django 3.1.2 on 2020-10-29 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20201029_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='tickets.ticket'),
        ),
    ]
