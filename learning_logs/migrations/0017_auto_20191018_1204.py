# Generated by Django 2.2.6 on 2019-10-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0016_auto_20191018_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
