# Generated by Django 2.2.6 on 2019-10-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_topic_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.TextField(),
        ),
    ]
