# Generated by Django 4.1 on 2022-08-28 02:07

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cat", "0001_add_str_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="image",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="/media/photos"
                ),
                upload_to="",
            ),
        ),
    ]
