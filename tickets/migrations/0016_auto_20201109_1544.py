# Generated by Django 3.1.3 on 2020-11-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_ticket_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='time',
            field=models.TimeField(null=True, verbose_name='Tempo Utilizado'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='deadline',
            field=models.DateTimeField(null=True, verbose_name='Prazo'),
        ),
    ]
