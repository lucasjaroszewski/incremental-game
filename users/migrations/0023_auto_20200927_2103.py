# Generated by Django 3.0.6 on 2020-09-28 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_character_character_weapon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='character_weapon',
            new_name='weapon',
        ),
    ]
