# Generated by Django 2.2.6 on 2020-02-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200228_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='Deliverd',
            field=models.BooleanField(default=True),
        ),
    ]
