# Generated by Django 3.2 on 2021-06-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0003_auto_20210613_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='philg',
            name='invitation',
            field=models.FileField(upload_to=''),
        ),
    ]
