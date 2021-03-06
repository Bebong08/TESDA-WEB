# Generated by Django 3.2 on 2021-06-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accredited_assesors', '0004_auto_20210612_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualifications', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='accredited_assesors',
            name='qualification',
        ),
        migrations.AddField(
            model_name='accredited_assesors',
            name='qualification',
            field=models.ManyToManyField(to='accredited_assesors.Qualifications'),
        ),
    ]
