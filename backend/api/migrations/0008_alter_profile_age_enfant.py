# Generated by Django 5.0.6 on 2024-06-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_full_name_profile_nom_enfant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age_enfant',
            field=models.IntegerField(),
        ),
    ]
