# Generated by Django 3.2.9 on 2021-11-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_blogpost_reposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='reposts',
            field=models.IntegerField(default=0),
        ),
    ]