# Generated by Django 3.1.7 on 2021-05-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0004_jobs_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='para2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='jobs',
            name='tags',
            field=models.CharField(default='', max_length=300),
        ),
    ]
