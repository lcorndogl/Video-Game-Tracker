# Generated by Django 4.2.17 on 2025-01-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_privacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='privacy',
            old_name='private',
            new_name='public',
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50)),
                ('platform', models.ManyToManyField(to='profiles.platforms')),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='game2',
            field=models.ManyToManyField(to='profiles.games'),
        ),
    ]
