# Generated by Django 3.1.2 on 2020-12-15 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0101_member_drugcd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='crimesDump',
        ),
    ]
