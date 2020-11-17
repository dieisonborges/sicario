# Generated by Django 3.1.3 on 2020-11-17 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0006_auto_20201116_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='after',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_after', to='equipments.equipment'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='before',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connection_before', to='equipments.equipment'),
        ),
    ]
