# Generated by Django 4.0.4 on 2022-06-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupin', '0002_merotime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merotime',
            name='create_at',
            field=models.DateTimeField(),
        ),
    ]