# Generated by Django 3.2 on 2021-04-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
