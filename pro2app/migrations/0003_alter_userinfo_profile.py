# Generated by Django 4.1 on 2023-04-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2app', '0002_alter_userinfo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile',
            field=models.ImageField(blank=True, upload_to='media/profiles/pic'),
        ),
    ]
