# Generated by Django 5.0.6 on 2024-06-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nom_tuteur',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('E', 'Encadreur'), ('P', 'Parent')], default='', max_length=1),
        ),
    ]
