# Generated by Django 3.0.3 on 2020-03-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('table', '0009_auto_20200320_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Сoefficient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_rate', models.FloatField(verbose_name='Коофециент')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_сoefficient', to='auth.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Коэффициент для группы',
                'verbose_name_plural': 'Коэффициенты для групп',
            },
        ),
    ]
