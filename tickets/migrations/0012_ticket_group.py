# Generated by Django 3.1.3 on 2020-11-09 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tickets', '0011_auto_20201108_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='group',
            field=models.ManyToManyField(related_name='groups', to='auth.Group'),
        ),
    ]
