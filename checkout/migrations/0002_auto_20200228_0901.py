# Generated by Django 2.2.6 on 2020-02-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='BookName',
        ),
        migrations.AddField(
            model_name='issue',
            name='Received',
            field=models.BooleanField(default=False),
        ),
    ]
