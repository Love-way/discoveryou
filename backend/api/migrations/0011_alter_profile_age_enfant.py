# Generated by Django 5.0.6 on 2024-06-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age_enfant',
            field=models.IntegerField(default=0),
        ),
    ]