# Generated by Django 3.2 on 2021-06-13 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_headlines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.RemoveField(
            model_name='news',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='news',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.RemoveField(
            model_name='news',
            name='headlines',
        ),
        migrations.RemoveField(
            model_name='news',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
