# Generated by Django 2.0.2 on 2018-02-13 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_edge_map'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edge',
            old_name='node_from',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='edge',
            old_name='node_to',
            new_name='target',
        ),
    ]
