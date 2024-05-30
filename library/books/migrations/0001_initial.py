# Generated by Django 5.0.6 on 2024-05-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtilte', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
