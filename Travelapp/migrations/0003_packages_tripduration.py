# Generated by Django 3.0.7 on 2020-07-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelapp', '0002_order_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='tripduration',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
