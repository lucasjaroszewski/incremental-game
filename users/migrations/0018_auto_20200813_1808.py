# Generated by Django 3.0.6 on 2020-08-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200807_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='stones',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
