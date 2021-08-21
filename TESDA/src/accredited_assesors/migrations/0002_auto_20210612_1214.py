# Generated by Django 3.2 on 2021-06-12 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accredited_assesors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualifications',
            name='centerclass',
        ),
        migrations.RemoveField(
            model_name='qualifications',
            name='trainingcenter',
        ),
        migrations.RenameField(
            model_name='accredited_assesors',
            old_name='address',
            new_name='Institution',
        ),
        migrations.RemoveField(
            model_name='accredited_assesors',
            name='qualification',
        ),
        migrations.AddField(
            model_name='accredited_assesors',
            name='qualification',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Center',
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
        migrations.DeleteModel(
            name='Qualifications',
        ),
    ]