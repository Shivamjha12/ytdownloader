# Generated by Django 3.1.7 on 2021-05-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0007_auto_20210518_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.CharField(default='5', max_length=100),
        ),
    ]