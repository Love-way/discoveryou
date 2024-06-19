# Generated by Django 5.0.6 on 2024-06-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_profile_age_enfant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Educateur', 'Educateur'), ('Parent', 'Parent')], max_length=10),
        ),
    ]