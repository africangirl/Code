# Generated by Django 5.0.6 on 2024-05-17 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='subtilte',
            new_name='subtitle',
        ),
    ]
