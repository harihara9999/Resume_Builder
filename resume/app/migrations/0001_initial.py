# Generated by Django 5.0.6 on 2024-07-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField()),
                ('college', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=20)),
                ('project', models.TextField()),
            ],
        ),
    ]
