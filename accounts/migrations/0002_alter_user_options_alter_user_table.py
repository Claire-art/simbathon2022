# Generated by Django 4.0.4 on 2022-07-08 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '유저', 'verbose_name_plural': '유저'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
