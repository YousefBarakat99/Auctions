# Generated by Django 4.2.2 on 2023-06-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auctions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]