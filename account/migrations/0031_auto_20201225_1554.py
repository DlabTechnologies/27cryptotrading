# Generated by Django 3.0.5 on 2020-12-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_newslettersignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='trade_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='trade_complete_message',
            field=models.CharField(default='Trade Completed', max_length=500),
        ),
    ]
