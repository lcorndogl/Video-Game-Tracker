# Generated by Django 4.2.17 on 2025-01-21 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_rename_profile_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='profile',
        ),
    ]
