# Generated by Django 2.2 on 2019-04-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0030_auto_20190425_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='reportNHits',
            field=models.IntegerField(default=0),
        ),
    ]
