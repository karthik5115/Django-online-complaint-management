# Generated by Django 4.1 on 2023-04-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2app', '0012_complaints_disliked_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='head',
            field=models.BooleanField(default=False),
        ),
    ]
