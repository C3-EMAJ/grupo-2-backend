# Generated by Django 4.0 on 2023-10-26 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendEMAJ', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pecas',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='name',
        ),
    ]
