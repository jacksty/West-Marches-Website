# Generated by Django 2.0.2 on 2018-02-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20180216_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='hidden',
            field=models.BooleanField(default=True),
        ),
    ]