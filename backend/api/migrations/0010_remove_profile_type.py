# Generated by Django 5.0.6 on 2024-06-16 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_profile_email_alter_profile_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='type',
        ),
    ]
