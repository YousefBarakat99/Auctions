# Generated by Django 3.0.14 on 2023-06-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20230620_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
