# Generated by Django 2.0.2 on 2018-04-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20180422_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
    ]