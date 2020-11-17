# Generated by Django 3.1.3 on 2020-11-17 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0009_auto_20201117_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='equipment_conected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_conected', to='equipments.equipment'),
        ),
    ]
