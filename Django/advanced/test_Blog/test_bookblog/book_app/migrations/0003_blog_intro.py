# Generated by Django 2.1.7 on 2019-04-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='intro',
            field=models.TextField(blank=True),
        ),
    ]
