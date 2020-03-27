from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

currency = (
        ('руб', 'руб'),
        ('usd', 'usd'),
        ('бел руб', 'бел руб')
    )

transmission = (
        ('МТ', 'МТ'),
        ('АТ', 'АТ'),
        ('Вариатор', 'Вариатор'),
        ('Робот', 'Робот')
    )

fuel = (
        ('бензин', 'бензин'),
        ('газ', 'газ'),
        ('гибрид', 'гибрид'),
        ('дизиль', 'дизиль')
    )

class Rate(models.Model):
    currency =  models.CharField(max_length=10, choices=currency, default='руб', verbose_name=_("Валюта"))
    currency_rate = models.FloatField(verbose_name=_("Курс валюты"))

    def __str__(self):
        return str(self.currency)

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = "Курс валют"

class Сoefficient(models.Model):
    group = models.OneToOneField(Group, on_delete = models.CASCADE, related_name='table_сoefficient', verbose_name=_("Группа"))
    coef = models.FloatField(verbose_name=_("Коофециент"))

    class Meta:
        verbose_name = 'Коэффициент для группы'
        verbose_name_plural = "Коэффициенты для групп"

class Сoefficient_guest(models.Model):
    coef = models.FloatField(verbose_name=_("Коофециент"))

    class Meta:
        verbose_name = 'Коэффициент для гостей'
        verbose_name_plural = "Коэффициенты для гостей"

class Table(models.Model):
    model_dvs = models.CharField(blank=True,null=True, max_length=50, verbose_name=_("Модель ДВС"))
    link = models.CharField(blank=True,null=True, max_length = 300, verbose_name=_("Ссылка"))
    price_without_c = models.DecimalField(blank=True,null=True,max_digits=10, decimal_places=0, verbose_name=_("Цена без навеса"))
    price_with_c = models.DecimalField(blank=True,null=True, max_digits=10, decimal_places=0, verbose_name=_("Цена с навесом"))
    currency =  models.CharField(blank=True,null=True,  max_length=10, choices=currency, default='руб', verbose_name=_("Валюта"))
    firm = models.CharField(blank=True,null=True, max_length=30, verbose_name=_("Фирма"))
    mark = models.CharField(blank=True,null=True, max_length=150, verbose_name=_("Марка"))
    model = models.CharField(blank=True,null=True, max_length=150, verbose_name=_("Модель"))
    body = models.CharField(blank=True,null=True, max_length=50, verbose_name=_("Кузов"))
    year =  models.CharField(blank=True,null=True, max_length=20, verbose_name=_("Год"))
    drive_unit = models.CharField(blank=True,null=True, max_length=50, verbose_name=_("Привод"))
    transmission = models.CharField(blank=True,null=True,  max_length=10, choices=transmission, default='МТ', verbose_name=_("КПП"))
    volume =  models.CharField(blank=True,null=True,max_length=20, verbose_name=_("Объем"))
    horsepower = models.CharField(blank=True,null=True, max_length=150, verbose_name=_("Количество ЛС"))
    fuel = models.CharField(blank=True,null=True,  max_length=10, choices=fuel, default='бензин', verbose_name=_("Топливо"))
    name = models.CharField(blank=True,null=True, max_length=300, verbose_name=_("Наименование"))
    information = models.TextField(blank=True,null=True, verbose_name=_("Информация"))
    number_dvs = models.CharField(blank=True,null=True, max_length=50, verbose_name=_("Номер ДВС"))
    number_oem = models.CharField(blank=True,null=True, max_length=50, verbose_name=_("Номер ОЕМ"))
    analog = models.CharField(blank=True,null=True, max_length=150, verbose_name=_("Аналог"))
    vin_code = models.CharField(blank=True,null=True, max_length=150, verbose_name=_("Vin код"))
    reliability = models.IntegerField(blank=True,null=True, verbose_name=_("Надежность поставки"))
    date_placement = models.DateField(blank=True,null=True, verbose_name=_("Дата размещения"))

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Двигатель'
        verbose_name_plural = "Двигатели"

class Permission(models.Model):
    group = models.OneToOneField(Group, on_delete = models.CASCADE, related_name='table_permission', verbose_name=_("Группа"))
    is_model_dvs = models.BooleanField(default=False , verbose_name=_("Модель ДВС"))
    is_link = models.BooleanField(default=False ,  verbose_name=_("Ссылка"))
    is_price_without_c =models.BooleanField(default=False ,  verbose_name=_("Цена без навеса"))
    is_price_with_c = models.BooleanField(default=False ,  verbose_name=_("Цена с навесом"))
    is_currency = models.BooleanField(default=False ,  verbose_name=_("Валюта"))
    is_firm = models.BooleanField(default=False ,  verbose_name=_("Фирма"))
    is_mark = models.BooleanField(default=False ,  verbose_name=_("Марка"))
    is_model = models.BooleanField(default=False ,  verbose_name=_("Модель"))
    is_body =models.BooleanField(default=False ,  verbose_name=_("Кузов"))
    is_year =  models.BooleanField(default=False ,  verbose_name=_("Год"))
    is_drive_unit = models.BooleanField(default=False ,  verbose_name=_("Привод"))
    is_transmission =models.BooleanField(default=False ,  verbose_name=_("КПП"))
    is_volume =  models.BooleanField(default=False ,  verbose_name=_("Объем"))
    is_horsepower = models.BooleanField(default=False ,  verbose_name=_("Количество ЛС"))
    is_fuel = models.BooleanField(default=False ,  verbose_name=_("Топливо"))
    is_name = models.BooleanField(default=False ,  verbose_name=_("Наименование"))
    is_information = models.BooleanField(default=False ,  verbose_name=_("Информация"))
    is_number_dvs = models.BooleanField(default=False , verbose_name=_("Номер ДВС"))
    is_number_oem = models.BooleanField(default=False ,  verbose_name=_("Номер ОЕМ"))
    is_analog = models.BooleanField(default=False ,  verbose_name=_("Аналог"))
    is_vin_code = models.BooleanField(default=False ,  verbose_name=_("Vin код"))
    is_reliability = models.BooleanField(default=False , verbose_name=_("Надежность поставки"))
    is_date_placement = models.BooleanField(default=False , verbose_name=_("Дата размещения"))

    class Meta:
        verbose_name = 'Права для групп'
        verbose_name_plural = "Права для групп"


class PermissionNone(models.Model):
    is_model_dvs = models.BooleanField(default=False , verbose_name=_("Модель ДВС"))
    is_link = models.BooleanField(default=False ,  verbose_name=_("Ссылка"))
    is_price_without_c =models.BooleanField(default=False ,  verbose_name=_("Цена без навеса"))
    is_price_with_c = models.BooleanField(default=False ,  verbose_name=_("Цена с навесом"))
    is_currency = models.BooleanField(default=False ,  verbose_name=_("Валюта"))
    is_firm = models.BooleanField(default=False ,  verbose_name=_("Фирма"))
    is_mark = models.BooleanField(default=False ,  verbose_name=_("Марка"))
    is_model = models.BooleanField(default=False ,  verbose_name=_("Модель"))
    is_body =models.BooleanField(default=False ,  verbose_name=_("Кузов"))
    is_year =  models.BooleanField(default=False ,  verbose_name=_("Год"))
    is_drive_unit = models.BooleanField(default=False ,  verbose_name=_("Привод"))
    is_transmission =models.BooleanField(default=False ,  verbose_name=_("КПП"))
    is_volume =  models.BooleanField(default=False ,  verbose_name=_("Объем"))
    is_horsepower = models.BooleanField(default=False ,  verbose_name=_("Количество ЛС"))
    is_fuel = models.BooleanField(default=False ,  verbose_name=_("Топливо"))
    is_name = models.BooleanField(default=False ,  verbose_name=_("Наименование"))
    is_information = models.BooleanField(default=False ,  verbose_name=_("Информация"))
    is_number_dvs = models.BooleanField(default=False , verbose_name=_("Номер ДВС"))
    is_number_oem = models.BooleanField(default=False ,  verbose_name=_("Номер ОЕМ"))
    is_analog = models.BooleanField(default=False ,  verbose_name=_("Аналог"))
    is_vin_code = models.BooleanField(default=False ,  verbose_name=_("Vin код"))
    is_reliability = models.BooleanField(default=False , verbose_name=_("Надежность поставки"))
    is_date_placement = models.BooleanField(default=False , verbose_name=_("Дата размещения"))

    class Meta:
        verbose_name = 'Права для гостей'
        verbose_name_plural = "Права для гостей"

class HomeTemplate(models.Model):
    group = models.OneToOneField(Group, on_delete = models.CASCADE, related_name='group_template', verbose_name=_("Группа"))
    template = models.TextField(verbose_name=_("Шаблон"))

    class Meta:
        verbose_name = 'Шаблон для групы'
        verbose_name_plural = "Шаблон для групп"

class HomeTemplateGuest(models.Model):
    template = models.TextField(verbose_name=_("Шаблон"))

    class Meta:
        verbose_name = 'Шаблон для гостя'
        verbose_name_plural = "Шаблон для гостей"


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_REAL_IP')
    if x_forwarded_for: 
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


#посылаем сигнал когда пользователь входит
from django.contrib.auth.signals import user_logged_in

def do_stuff(sender, user, request, **kwargs):
    ip = get_client_ip(request)
    useragent = request.META['HTTP_USER_AGENT']
    new_log = AuntificationLog.objects.create(user = user, useragent=useragent, ip=ip, action = 'login')

user_logged_in.connect(do_stuff)

class AuntificationLog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_log', verbose_name=_("Пользователь"))
    useragent = models.CharField(max_length=500, default = '', verbose_name=_("UserAgent"))
    date = models.DateTimeField( auto_now_add = True, verbose_name=_("Дата"))
    ip = models.CharField(max_length=20,  verbose_name=_("IP"))
    action = models.CharField(max_length=300, default = '', verbose_name=_("Действие"))


    class Meta:
        ordering = ["-id"]
        verbose_name = 'Лог'
        verbose_name_plural = "Лог авторизаций"