# Generated by Django 4.2 on 2023-05-09 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_continent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='mapsURL',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.continent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='mapsURL',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='continent',
            name='image',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
    ]
