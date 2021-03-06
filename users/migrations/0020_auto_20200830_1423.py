# Generated by Django 3.0.6 on 2020-08-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20200830_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='loot',
        ),
        migrations.AddField(
            model_name='fish',
            name='loot',
            field=models.ManyToManyField(default=None, null=True, related_name='loots', to='users.Loot'),
        ),
        migrations.RemoveField(
            model_name='fish',
            name='weapon',
        ),
        migrations.AddField(
            model_name='fish',
            name='weapon',
            field=models.ManyToManyField(default=None, null=True, related_name='weapons', to='users.Weapon'),
        ),
    ]
