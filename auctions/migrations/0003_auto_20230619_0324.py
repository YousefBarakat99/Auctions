# Generated by Django 3.0.14 on 2023-06-19 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctions_bid_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='active',
        ),
        migrations.RemoveField(
            model_name='auctions',
            name='category',
        ),
        migrations.RemoveField(
            model_name='auctions',
            name='date',
        ),
    ]
