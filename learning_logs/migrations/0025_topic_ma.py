# Generated by Django 2.2.6 on 2019-10-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0024_auto_20191018_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='ma',
            field=models.EmailField(default='a@163.com', max_length=254),
        ),
    ]
