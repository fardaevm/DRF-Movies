# Generated by Django 5.0.7 on 2024-09-19 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='updated_at',
            new_name='updated_date',
        ),
    ]