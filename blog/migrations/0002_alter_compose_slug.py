# Generated by Django 3.2.9 on 2021-11-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compose',
            name='slug',
            field=models.SlugField(max_length=1000, unique_for_date='publish'),
        ),
    ]
