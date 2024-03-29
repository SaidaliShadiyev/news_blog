# Generated by Django 5.0.2 on 2024-03-06 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_remove_news_content_alter_news_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_app.news'),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(default='abc'),
            preserve_default=False,
        ),
    ]
