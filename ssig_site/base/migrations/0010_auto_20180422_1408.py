# Generated by Django 2.0.2 on 2018-04-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20180418_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='long_description',
            field=models.TextField(blank=True),
        ),
    ]
