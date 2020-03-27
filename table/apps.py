from django.apps import AppConfig


class TableConfig(AppConfig):
    name = 'table'
    verbose_name =  u"Таблица"

class PermissionConfig(AppConfig):
    name = 'permission'
    verbose_name =  u"Права на просмотр талицы"