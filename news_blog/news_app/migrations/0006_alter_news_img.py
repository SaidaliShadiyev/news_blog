# Generated by Django 5.0.2 on 2024-03-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_alter_news_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
