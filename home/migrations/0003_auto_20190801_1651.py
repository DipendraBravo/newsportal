# Generated by Django 2.1.1 on 2019-08-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190801_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='category',
            field=models.TextField(default='business'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='sources',
            field=models.TextField(default='bbc-news'),
        ),
    ]
