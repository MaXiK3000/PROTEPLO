# Generated by Django 4.2.15 on 2024-09-21 13:26

from django.db import migrations, models
import proteplo_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('proteplo_app', '0013_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=proteplo_app.models.get_image_upload_path),
        ),
    ]
