# Generated by Django 3.0.3 on 2020-03-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tell',
            field=models.TextField(default='-'),
        ),
    ]
