# Generated by Django 4.0.6 on 2022-07-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_freepost_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='freepost',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
