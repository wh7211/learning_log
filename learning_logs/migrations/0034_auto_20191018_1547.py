# Generated by Django 2.2.6 on 2019-10-18 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0033_auto_20191018_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='ma',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='myt',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='ppp',
        ),
    ]
