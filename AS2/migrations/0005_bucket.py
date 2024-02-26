# Generated by Django 5.0.2 on 2024-02-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AS2', '0004_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('bucket_type', models.CharField(max_length=50)),
                ('bucket_id', models.IntegerField()),
            ],
        ),
    ]
