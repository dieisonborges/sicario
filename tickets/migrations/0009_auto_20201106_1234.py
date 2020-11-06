# Generated by Django 3.1.2 on 2020-11-06 12:34

from django.db import migrations, models
import tickets.utils


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20201103_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='docfile',
            field=models.FileField(null=True, upload_to=tickets.utils.path_and_rename),
        ),
        migrations.AddField(
            model_name='ticket',
            name='docfile',
            field=models.FileField(null=True, upload_to=tickets.utils.path_and_rename),
        ),
    ]