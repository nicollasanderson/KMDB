# Generated by Django 4.0.5 on 2022-06-27 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
