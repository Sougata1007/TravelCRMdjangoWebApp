# Generated by Django 3.0.7 on 2020-07-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelapp', '0006_auto_20200701_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
