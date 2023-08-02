# Generated by Django 4.2.3 on 2023-08-01 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=True, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('instructor', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('tagline', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.IntegerField(default=0)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=10)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnails')),
                ('resource', models.FileField(upload_to='files/resources')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.category')),
            ],
        ),
    ]
