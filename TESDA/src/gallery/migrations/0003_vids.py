# Generated by Django 3.2 on 2021-06-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_gallery_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slider', models.BooleanField(default=True)),
            ],
        ),
    ]
