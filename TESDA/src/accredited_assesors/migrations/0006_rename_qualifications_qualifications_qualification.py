# Generated by Django 3.2 on 2021-06-12 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accredited_assesors', '0005_auto_20210612_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qualifications',
            old_name='Qualifications',
            new_name='qualification',
        ),
    ]