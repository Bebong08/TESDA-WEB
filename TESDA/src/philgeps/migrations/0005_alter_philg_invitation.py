# Generated by Django 3.2 on 2021-06-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0004_alter_philg_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='philg',
            name='invitation',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
