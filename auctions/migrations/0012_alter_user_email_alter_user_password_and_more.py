# Generated by Django 4.2.2 on 2023-06-20 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True),
        ),
    ]
