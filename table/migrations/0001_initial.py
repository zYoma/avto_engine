# Generated by Django 3.0.3 on 2020-03-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_dvs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Модель ДВС')),
                ('link', models.URLField(blank=True, max_length=300, null=True, verbose_name='Ссылка')),
                ('price_without_c', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Цена без навеса')),
                ('price_with_c', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Цена с навесом')),
                ('currency', models.CharField(blank=True, choices=[('руб', 'руб'), ('usd', 'usd'), ('бел руб', 'бел руб')], default='руб', max_length=10, null=True, verbose_name='Валюта')),
                ('firm', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фирма')),
                ('mark', models.CharField(blank=True, max_length=150, null=True, verbose_name='Марка')),
                ('model', models.CharField(blank=True, max_length=150, null=True, verbose_name='Модель')),
                ('body', models.CharField(blank=True, max_length=50, null=True, verbose_name='Кузов')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('drive_unit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Привод')),
                ('transmission', models.CharField(blank=True, choices=[('МТ', 'МТ'), ('АТ', 'АТ'), ('Вариатор', 'Вариатор'), ('Робот', 'Робот')], default='МТ', max_length=10, null=True, verbose_name='КПП')),
                ('volume', models.FloatField(blank=True, null=True, verbose_name='Объем')),
                ('horsepower', models.CharField(blank=True, max_length=150, null=True, verbose_name='Количество ЛС')),
                ('fuel', models.CharField(blank=True, choices=[('бензин', 'бензин'), ('газ', 'газ'), ('гибрид', 'гибрид'), ('дизиль', 'дизиль')], default='бензин', max_length=10, null=True, verbose_name='Топливо')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Наименование')),
                ('information', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('number_dvs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер ДВС')),
                ('number_oem', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер ОЕМ')),
                ('analog', models.CharField(blank=True, max_length=150, null=True, verbose_name='Аналог')),
                ('vin_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='Vin код')),
                ('is_photo', models.BooleanField(default=False, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Таблица двигателей',
                'verbose_name_plural': 'Таблица двигателей',
                'ordering': ['-id'],
            },
        ),
    ]
