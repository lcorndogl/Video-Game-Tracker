# Generated by Django 4.2.17 on 2025-01-15 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_game_platform_favourite_game2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='platform2',
        ),
        migrations.AddField(
            model_name='favourite',
            name='platform2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.platform'),
            preserve_default=False,
        ),
    ]
