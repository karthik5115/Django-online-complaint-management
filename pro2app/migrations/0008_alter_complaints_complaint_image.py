# Generated by Django 4.1 on 2023-04-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro2app', '0007_alter_complaints_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='complaint_image',
            field=models.ImageField(upload_to='media/complaintpics'),
        ),
    ]
