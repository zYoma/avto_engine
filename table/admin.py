from django.contrib import admin
from .models import *

class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_dvs', 'link', 'price_without_c', 'price_with_c', 'currency','firm', 'mark', 'model', 'body', 'year', 'drive_unit','transmission', 'volume', 'horsepower', 'fuel', 'name', 'information','number_dvs', 'number_oem', 'analog', 'vin_code', 'reliability', 'date_placement')
    search_fields = ('model_dvs','firm', 'mark', 'model','vin_code')
    list_filter = ("currency", "transmission", "fuel")
    empty_value_display = '-пусто-'

admin.site.register(Table, TableAdmin)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('group', 'is_model_dvs', 'is_link', 'is_price_without_c', 'is_price_with_c', 'is_currency','is_firm', 'is_mark', 'is_model', 'is_body', 'is_year', 'is_drive_unit','is_transmission', 'is_volume', 'is_horsepower', 'is_fuel', 'is_name', 'is_information','is_number_dvs', 'is_number_oem', 'is_analog', 'is_vin_code', 'is_reliability', 'is_date_placement')

admin.site.register(Permission, PermissionAdmin)

class PermissionNoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_model_dvs', 'is_link', 'is_price_without_c', 'is_price_with_c', 'is_currency','is_firm', 'is_mark', 'is_model', 'is_body', 'is_year', 'is_drive_unit','is_transmission', 'is_volume', 'is_horsepower', 'is_fuel', 'is_name', 'is_information','is_number_dvs', 'is_number_oem', 'is_analog', 'is_vin_code', 'is_reliability', 'is_date_placement')

admin.site.register(PermissionNone, PermissionNoneAdmin)

class RateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'currency_rate')
    
admin.site.register(Rate, RateAdmin)

class СoefficientAdmin(admin.ModelAdmin):
    list_display = ('group', 'coef')
    
admin.site.register(Сoefficient, СoefficientAdmin)

class Сoefficient_guestAdmin(admin.ModelAdmin):
    list_display = ('id', 'coef')
    
admin.site.register(Сoefficient_guest, Сoefficient_guestAdmin)

class HomeTemplateGuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'template')
    
admin.site.register(HomeTemplateGuest, HomeTemplateGuestAdmin)

class HomeTemplateAdmin(admin.ModelAdmin):
    list_display = ('group', 'template')
    
admin.site.register(HomeTemplate, HomeTemplateAdmin)

class AuntificationLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'user','ip', 'action',  'useragent')
    search_fields = ('user__username','ip')
    list_filter = ('date', 'user', 'action', 'ip', 'useragent')
    
admin.site.register(AuntificationLog, AuntificationLogAdmin)
