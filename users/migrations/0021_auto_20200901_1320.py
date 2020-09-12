# Generated by Django 3.0.6 on 2020-09-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200830_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='c_stones',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='absorb',
            field=models.CharField(blank=True, default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='fish',
            name='loot',
            field=models.ManyToManyField(blank=True, default=None, related_name='loots', to='users.Loot'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='resist',
            field=models.CharField(blank=True, default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='fish',
            name='weak',
            field=models.CharField(blank=True, default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='fish',
            name='weapon',
            field=models.ManyToManyField(blank=True, default=None, related_name='weapons', to='users.Weapon'),
        ),
    ]
