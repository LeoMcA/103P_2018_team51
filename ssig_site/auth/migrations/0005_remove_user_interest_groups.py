# Generated by Django 2.0.2 on 2018-03-15 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssig_site_auth', '0004_auto_20180310_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='interest_groups',
        ),
    ]