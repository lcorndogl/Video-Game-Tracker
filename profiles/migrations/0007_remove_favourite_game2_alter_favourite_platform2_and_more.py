# Generated by Django 4.2.17 on 2025-01-15 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_favourite_platform2_favourite_platform2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='game2',
        ),
        migrations.AlterField(
            model_name='favourite',
            name='platform2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.platform'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='game2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='profiles.game'),
            preserve_default=False,
        ),
    ]
