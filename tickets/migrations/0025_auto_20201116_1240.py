# Generated by Django 3.1.3 on 2020-11-16 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0024_ticket_equipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='equipment',
            new_name='equipments',
        ),
    ]
