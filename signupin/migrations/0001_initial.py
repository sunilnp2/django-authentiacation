# Generated by Django 4.0.4 on 2022-05-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('hidden', models.CharField(max_length=20)),
                ('tick', models.BooleanField(default=False)),
            ],
        ),
    ]
