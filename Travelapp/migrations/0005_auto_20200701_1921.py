# Generated by Django 3.0.7 on 2020-07-01 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travelapp', '0004_packages_destination'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='place_name',
            new_name='pack_name',
        ),
    ]
