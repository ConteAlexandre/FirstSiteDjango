# Generated by Django 3.0.3 on 2020-03-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200302_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
