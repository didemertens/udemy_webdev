# Generated by Django 2.1.7 on 2019-03-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20190324_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='email', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='verify_email',
            field=models.EmailField(default='email', max_length=100),
        ),
    ]
