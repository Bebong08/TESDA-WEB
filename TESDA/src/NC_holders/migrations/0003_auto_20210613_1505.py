# Generated by Django 3.2 on 2021-06-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NC_holders', '0002_remove_ncholders_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncholders',
            name='date_released',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ncholders',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]