# Generated by Django 3.0.7 on 2020-07-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelapp', '0003_packages_tripduration'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='destination',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
