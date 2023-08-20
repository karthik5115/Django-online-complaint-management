# Generated by Django 4.1 on 2023-04-24 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pro2app', '0005_complaints'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='village',
            new_name='location',
        ),
        migrations.AddField(
            model_name='complaints',
            name='city',
            field=models.CharField(default='eluru', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]