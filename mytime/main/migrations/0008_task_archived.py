# Generated by Django 2.2 on 2019-06-06 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190605_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
