# Generated by Django 3.0.5 on 2020-10-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20201027_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='place_on_hold',
            field=models.BooleanField(default=False),
        ),
    ]
