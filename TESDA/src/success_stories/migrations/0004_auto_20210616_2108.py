# Generated by Django 3.2 on 2021-06-16 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('success_stories', '0003_rename_name_stories_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='timestamp',
            new_name='caption',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='story',
        ),
        migrations.AddField(
            model_name='stories',
            name='vids',
            field=models.FileField(default=django.utils.timezone.now, upload_to='videos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stories',
            name='title',
            field=models.TextField(),
        ),
    ]
