# Generated by Django 4.1 on 2023-04-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2app', '0009_complaints_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='dislikes',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='complaints',
            name='likes',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
