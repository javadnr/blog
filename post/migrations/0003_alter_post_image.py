# Generated by Django 4.1.2 on 2022-10-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images'),
        ),
    ]
