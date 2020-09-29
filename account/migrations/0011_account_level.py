# Generated by Django 3.0.5 on 2020-08-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_userdepositrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silver_min', models.CharField(blank=True, max_length=100)),
                ('silver_max', models.CharField(blank=True, max_length=100)),
                ('silver_duration', models.CharField(blank=True, max_length=100)),
                ('silver_profit', models.CharField(blank=True, max_length=100)),
                ('gold_min', models.CharField(blank=True, max_length=100)),
                ('gold_max', models.CharField(blank=True, max_length=100)),
                ('gold_duration', models.CharField(blank=True, max_length=100)),
                ('gold_profit', models.CharField(blank=True, max_length=100)),
                ('platinum_min', models.CharField(blank=True, max_length=100)),
                ('platinum_max', models.CharField(blank=True, max_length=100)),
                ('platinum_duration', models.CharField(blank=True, max_length=100)),
                ('platinum_profit', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
