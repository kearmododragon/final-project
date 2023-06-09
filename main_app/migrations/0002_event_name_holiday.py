# Generated by Django 4.2 on 2023-05-10 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='event', max_length=100),
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='holiday', max_length=100)),
                ('arrivalDate', models.DateField(auto_now=True, verbose_name='Left home')),
                ('deparureDate', models.DateField(auto_now=True, verbose_name='Returned')),
                ('companions', models.CharField(default='friend', max_length=1000)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
