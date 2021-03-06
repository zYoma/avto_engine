# Generated by Django 3.0.3 on 2020-03-21 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table', '0014_auto_20200321_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuntificationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useragent', models.CharField(default='', max_length=500, verbose_name='UserAgent')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='IP')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_log', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Лог авторизаций',
                'ordering': ['id'],
            },
        ),
    ]
