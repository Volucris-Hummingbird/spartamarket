# Generated by Django 4.2 on 2024-04-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_remove_article_like_user_article_like_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
