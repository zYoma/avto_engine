# Generated by Django 3.0.3 on 2020-03-26 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0017_auto_20200321_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auntificationlog',
            options={'ordering': ['-id'], 'verbose_name': 'Лог', 'verbose_name_plural': 'Лог авторизаций'},
        ),
    ]