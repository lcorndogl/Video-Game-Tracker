# Generated by Django 4.2.17 on 2025-01-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_favourite_game2_alter_favourite_platform2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='game2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.game'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='platform2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.platform'),
        ),
    ]
