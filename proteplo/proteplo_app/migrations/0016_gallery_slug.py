# Generated by Django 4.2.15 on 2024-09-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteplo_app', '0015_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
