# Generated by Django 3.2.9 on 2021-12-21 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20211221_1608'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Anime',
            new_name='Movie',
        ),
        migrations.DeleteModel(
            name='Cartoon',
        ),
    ]
