# Generated by Django 4.1.3 on 2023-02-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_image_image_image_created_at_image_image_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]