# Generated by Django 3.2 on 2021-05-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slider',
            field=models.BooleanField(default=True),
        ),
    ]