# Generated by Django 2.2.6 on 2019-10-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0013_auto_20191018_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.BooleanField(verbose_name='False'),
        ),
    ]
