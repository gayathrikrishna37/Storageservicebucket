# Generated by Django 5.0.2 on 2024-02-26 07:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AS2', '0005_bucket'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='bucket',
            name='updation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
