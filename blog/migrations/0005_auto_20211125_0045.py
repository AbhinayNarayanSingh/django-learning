# Generated by Django 3.2.9 on 2021-11-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211125_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compose',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='compose',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]