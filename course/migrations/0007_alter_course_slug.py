# Generated by Django 4.2.3 on 2023-08-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
