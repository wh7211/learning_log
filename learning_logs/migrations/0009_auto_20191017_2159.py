# Generated by Django 2.2.6 on 2019-10-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0008_auto_20191017_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.TextField(),
        ),
    ]
