# Generated by Django 4.2.15 on 2024-09-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteplo_app', '0008_gallery_image_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=models.CharField(blank=True, max_length=100)),
        ),
    ]
