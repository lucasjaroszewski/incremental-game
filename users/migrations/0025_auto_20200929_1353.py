# Generated by Django 3.0.6 on 2020-09-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_character_dgn_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='weapon',
        ),
        migrations.AddField(
            model_name='character_weapon',
            name='weapon',
            field=models.ManyToManyField(related_name='weapon', to='users.Character'),
        ),
    ]
