# Generated by Django 3.0.6 on 2020-10-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20201003_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='badge',
            field=models.CharField(default='', max_length=3),
        ),
    ]
