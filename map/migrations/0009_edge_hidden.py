# Generated by Django 2.0.2 on 2018-02-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20180216_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='edge',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
