# Generated by Django 5.0 on 2023-12-06 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myblogApp", "0002_post_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["date_posted"]},
        ),
    ]
