# Generated by Django 2.1.7 on 2019-03-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verify_email',
            field=models.EmailField(default='password', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
