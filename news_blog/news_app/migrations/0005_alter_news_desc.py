# Generated by Django 5.0.2 on 2024-03-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_alter_news_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]