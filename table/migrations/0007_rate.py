# Generated by Django 3.0.3 on 2020-03-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_auto_20200316_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('руб', 'руб'), ('usd', 'usd'), ('бел руб', 'бел руб')], default='руб', max_length=10, verbose_name='Валюта')),
                ('currency_rate', models.FloatField(verbose_name='Курс валюты')),
            ],
            options={
                'verbose_name': 'Курс валюты',
                'verbose_name_plural': 'Курс валют',
            },
        ),
    ]
