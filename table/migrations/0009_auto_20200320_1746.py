# Generated by Django 3.0.3 on 2020-03-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0008_auto_20200320_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='is_photo',
        ),
        migrations.RemoveField(
            model_name='permissionnone',
            name='is_photo',
        ),
        migrations.AddField(
            model_name='permission',
            name='is_date_placement',
            field=models.BooleanField(default=False, verbose_name='Дата размещения'),
        ),
        migrations.AddField(
            model_name='permission',
            name='is_reliability',
            field=models.BooleanField(default=False, verbose_name='Надежность поставки'),
        ),
        migrations.AddField(
            model_name='permissionnone',
            name='is_date_placement',
            field=models.BooleanField(default=False, verbose_name='Дата размещения'),
        ),
        migrations.AddField(
            model_name='permissionnone',
            name='is_reliability',
            field=models.BooleanField(default=False, verbose_name='Надежность поставки'),
        ),
    ]
