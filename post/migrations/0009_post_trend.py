# Generated by Django 4.2.6 on 2023-11-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='trend',
            field=models.BooleanField(default=False),
        ),
    ]
