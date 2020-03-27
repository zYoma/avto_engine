from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth import get_user_model
#from .forms import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.core.paginator import Paginator
from import_csv import upload_table
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models import Avg, Max, Min
from django.db.models import Func
import re
from itertools import chain
from django.utils.decorators import method_decorator
from table.utils import write_log


re_pattern = r'\s+|\W+|_'
re_start_word = r"(^|\s)%s"

User = get_user_model()

class Round(Func):
  function = 'ROUND'
  arity = 2

def get_model_fields(model):
    table_fields = [f.name for f in model._meta.fields]
    return table_fields


def get_field_values(field):
    filter = field
    field_list = Table.objects.all().exclude(**{filter: ''}).values_list(field, flat = True)
    field_list = list(set(field_list))
    field_list = sorted(field_list)
    return field_list


def page_not_found(request, exception):
    return render(request, "misc/404.html", {"path": request.path}, status=404)

def server_error(request):
    return render(request, "misc/500.html", status=500)

def clear_data(all_table,table_fields, clear_pattern, property):

    clear_dict = {}
    for  obj in all_table:
        for field in table_fields:
            if field == property:
                clear_obj = re.sub(re_pattern, '', str(getattr( obj , field )))

        clear_dict[obj.id] = clear_obj.lower()

    num_list = [key for key in clear_dict if clear_pattern in clear_dict[key]]
    return num_list


def gen_table(all_table, num_list):
    result_list = []
    for obj in all_table:
        for n in num_list:
            if obj.id == n:
                result_list.append(obj.id)

    all_table = Table.objects.filter(id__in = result_list)
    return all_table


def convert_currency(request, all_table, group_name = None):
    if group_name:
        if group_name == 'user':
            coef = Сoefficient.objects.all().first().coef

        else:
            coef = 1
    else:
        coef = Сoefficient_guest.objects.all().first().coef



    price_list = []
    for obj in all_table:
        if obj.currency != 'руб' and obj.currency != 0:
            try:
                currency = Rate.objects.get(currency = obj.currency)
            except:
                obj.price_without_c = 0
                obj.price_with_c = 0
            else:
                obj.price_without_c = round(float(obj.price_without_c) * currency.currency_rate)
                obj.price_with_c = round(float(obj.price_with_c) * currency.currency_rate)

        #умножаем на кооф

        if group_name == 'user' or group_name == None:
            obj.price_without_c = round(round(float(obj.price_without_c) * coef, -2))
            obj.price_with_c = round(round(float(obj.price_with_c) * coef, -2))
        else:
            obj.price_without_c = round(float(obj.price_without_c) * coef)
            obj.price_with_c = round(float(obj.price_with_c) * coef)

        #собираем цены дя подсчета среднего
        if obj.price_without_c == 0:
            if obj.price_with_c != 0:
                price_list.append(obj.price_with_c)
        else:
            price_list.append(obj.price_without_c)

    
    price = calculation(price_list)

    return all_table, price

def calculation(price_list):

    if len(price_list) > 0:
        max_value = max(price_list)
        min_value = min(price_list)
        avg_value = round(sum(price_list)/len(price_list))

        price = {
            'avg_price': avg_value,
            'min_price': min_value,
            'max_price': max_value

        }
    else:
        price = None

    return price

def correct_price(all_table):
    price_list = []
    for obj in all_table:
         #собираем цены дя подсчета среднего
        if obj.price_without_c == 0:
            if obj.price_with_c != 0:
                price_list.append(obj.price_with_c)
        else:
            price_list.append(obj.price_without_c)
    
    price = calculation(price_list)

    return price


def find_sartword(property, clear_pattern, table_fields,all_table):
    text = re.escape(clear_pattern)
    for field in table_fields:
        if field == property:
            all_table = [obj for obj in all_table if re.search(re_start_word % text, str(getattr( obj , field )))]

   

    return all_table
    

def obj_list(request, all_table, table_fields,group_name,pattern, property):

    pattern_dict, clear_pattern = clearing_pattern(pattern, low=True)

    if len(clear_pattern) < 3:
        all_table = find_sartword(property,clear_pattern, table_fields, all_table  )
        if len(all_table) > 0:
            all_table, price = convert_currency(request, all_table, group_name)
        else:
            price = None
            all_table =[]
    else:
        num_list = clear_data(all_table,table_fields, clear_pattern, property)

        if len(num_list) > 0:
            all_table = gen_table(all_table, num_list)
            all_table, price = convert_currency(request, all_table, group_name)
        else:
            price = None
            all_table =[]

    return all_table, price

@method_decorator(write_log, name='dispatch')
class Index(View):
    def get(self, request):
        
        if request.user.is_authenticated:
            group_name= request.user.groups.first().name
            if group_name == 'user':
                index_template = HomeTemplate.objects.get(group__name='user').template
            elif group_name == 'manager':
                index_template = HomeTemplate.objects.get(group__name='manager').template
            elif request.user.is_staff:
                index_template = None
        else:
            index_template = HomeTemplateGuest.objects.all().first().template

        return render(request, 'table/index.html', context = {'index_template':index_template})


def clearing_pattern(pattern, low=False):
    pattern_dict = {}
    if low:
        pattern = pattern.lower()
    pattern_dict['search'] = pattern
    clear_pattern = re.sub(re_pattern, '', pattern)

    return pattern_dict, clear_pattern


@method_decorator(write_log, name='dispatch')
class Search(View):
    def get(self, request):
#----------------------Группы и права-------------------------------------------------------------
        if request.user.is_authenticated:
            #group_name = request.user.groups.values_list('name',flat = True) # QuerySet 
            group_name= request.user.groups.first().name
            #groups = list(group_name)
            group = Permission.objects.get(group__name=group_name)
            guest_permission = None
        else:
            group_name = None
            group = None
            guest_permission = PermissionNone.objects.all().first()
##-------------------------------------Общие переменны--------------------------------------
        
        price = None
        pattern_dict = {}
        all_table =[]
        volums_list = get_field_values(field='volume')
        transmission_list = get_field_values(field='transmission')
        fuel_list = get_field_values(field='fuel')
        table_fields = get_model_fields(Table)

##-------------------------------------Поиск--------------------------------------
        pattern = request.GET['search']
        pattern_dict, clear_pattern = clearing_pattern(pattern, low=True)
        #если поисковой запрос менее 3 символов то будем искать с начала слова
        if len(clear_pattern) < 3:
            text = re.escape(clear_pattern) # make sure there are not regex specials
            all_table = Table.objects.filter(Q(model_dvs__iregex=re_start_word % text) | Q(information__iregex=re_start_word % text) | Q(number_dvs__iregex=re_start_word % text)| Q(number_oem__iregex=re_start_word % text) | Q(analog__iregex=re_start_word % text) | Q(name__iregex=re_start_word % text) )
            if len(all_table) > 0:
                all_table, price = convert_currency(request, all_table, group_name)
            else:
                all_table =[]

        else:
            all_table = Table.objects.all()
            num_list1 = clear_data(all_table,table_fields, clear_pattern, property = 'model_dvs')
            num_list2 = clear_data(all_table,table_fields, clear_pattern, property = 'information')
            num_list3 = clear_data(all_table,table_fields, clear_pattern, property = 'number_dvs')
            num_list4 = clear_data(all_table,table_fields, clear_pattern, property = 'number_oem')
            num_list5 = clear_data(all_table,table_fields, clear_pattern, property = 'analog')
            num_list6 = clear_data(all_table,table_fields, clear_pattern, property = 'name')
            num_list = num_list1 + num_list2 + num_list3 + num_list4 + num_list5 + num_list6
            
            if len(num_list) > 0:
                all_table = gen_table(all_table, num_list)
                all_table, price = convert_currency(request, all_table, group_name)
            else:
                all_table =[]   

##-------------------------------------Фильтры--------------------------------------
        if 'filter' in request.GET:

            search_property = [
                        'model_dvs',
                        'link',
                        'currency',
                        'firm',
                        'mark',
                        'model',
                        'body',
                        'year',
                        'drive_unit',
                        'horsepower',
                        'name',
                        'information',
                        'number_dvs',
                        'number_oem',
                        'analog',
                        'vin_code'

                    ]
            for property in search_property:
                if property in request.GET and request.GET[property] != '':
                    pattern = request.GET[property]
                    pattern_dict[property] = pattern
                    all_table, price = obj_list(request, all_table, table_fields,group_name,pattern, property = property) 

##-------------------------------------Выборка--------------------------------------
        if 'sample' in request.GET:

            sample =[ 'price_min','price_max','price_2_min','price_2_max','transmission','fuel', 'volume','min_reliability','max_reliability']
            for item in sample:

                if item in request.GET and request.GET[item] != 'Все' and request.GET[item] != '':
                    pattern = request.GET[item]

                    pattern_dict[item] = pattern
                    if item == 'transmission':
                        all_table = [obj for obj in all_table if obj.transmission == pattern]
                    elif item == 'fuel':
                        all_table = [obj for obj in all_table if obj.fuel == pattern]
                    elif item == 'volume':
                        all_table = [obj for obj in all_table if obj.volume == pattern]
                

                    elif item == 'price_min': 
                        all_table = [obj for obj in all_table if obj.price_without_c >= int(pattern)]
                        # all_table = all_table.filter(price_without_c__gte=int(pattern))
                    elif item == 'price_max':       
                        all_table = [obj for obj in all_table if obj.price_without_c <= int(pattern)]
                    elif item == 'price_2_min':
                        all_table = [obj for obj in all_table if obj.price_with_c >= int(pattern)]
                    elif item == 'price_2_max':   
                        all_table = [obj for obj in all_table if obj.price_with_c <= int(pattern)]

                    elif item == 'min_reliability':   
                        all_table = [obj for obj in all_table if obj.reliability >= int(pattern)]

                    elif item == 'max_reliability':  
                        all_table = [obj for obj in all_table if obj.reliability <= int(pattern)]

            price = correct_price(all_table)
            #all_table, price = convert_currency(request, all_table, group_name)  

##-------------------------------------Сортировка--------------------------------------
        if 'sort' in request.GET and len(all_table) > 0:
            pattern = request.GET['sort']
            pattern_dict['sort'] = pattern
            if pattern == 'price_desc':
                all_table = sorted(all_table, key=lambda x: x.price_without_c   , reverse=True)
            elif pattern == 'price_asc':
                all_table = sorted(all_table, key=lambda x: (x.price_without_c == 0, x.price_without_c) )     
            elif pattern == 'price_2_desc':
                all_table = sorted(all_table, key=lambda x: x.price_with_c, reverse=True) 
            elif pattern == 'price_2_asc':
                all_table = sorted(all_table, key=lambda x: (x.price_with_c == 0, x.price_with_c)) 
            elif pattern == 'reliability_desc':
                all_table = sorted(all_table, key=lambda x: x.reliability , reverse=True) 
            elif pattern == 'reliability_asc':
                all_table = sorted(all_table, key=lambda x: x.reliability) 
            elif pattern == 'date_placement_asc':
                all_table = sorted(all_table, key=lambda x: x.date_placement) 
            elif pattern == 'date_placement_desc':
                all_table = sorted(all_table, key=lambda x: x.date_placement, reverse=True) 




##-------------------------------------Пагинатор--------------------------------------
        get_copy = request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
        paginator = Paginator(all_table, 50)
        last_page = paginator.num_pages
        page_number = request.GET.get('page', 1) #Получаем из адресной строки значение для page. Если его нет, то -1
        page = paginator.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url='?page={}'.format(page.previous_page_number())
        else:
            prev_url=''

        if page.has_next():
            next_url= '?page={}'.format(page.next_page_number())
        else:
            next_url=''

        return render(request, 'table/index.html', context = {'group_name':group_name, 'fuel_list':fuel_list,'transmission_list':transmission_list,'volums_list': volums_list, 'pattern_dict': pattern_dict, 'price':price, 'guest_permission':guest_permission,'group':group,'table': page, 'is_paginator':is_paginator, 'prev_url':prev_url, 'next_url':next_url, 'parameters':parameters, 'page_end': last_page})


class Upload(View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'table/upload.html')
        else:
            return HttpResponse('<h1>Вы не имеете доступа к этой странице</h1>')

    def post(self, request):
        if not request.user.is_staff:
            return HttpResponse('<h1>Вы не имеете доступа к этой странице</h1>')

        if 'table'  in request.FILES:
            csv_file = request.FILES['table']
            ext = csv_file.name.split('.')[-1]
            if ext != 'csv':
                return HttpResponse('<h1>Талица должна быть в формате CSV (cp1251, разделитель - ;)</h1>')
            fs = FileSystemStorage(location='media/table/') #defaults to   MEDIA_ROOT  
            fullname = os.path.join(settings.MEDIA_ROOT,'table/', csv_file.name)
            if os.path.exists(fullname):
                os.remove(fullname)

            fs.save(csv_file.name, csv_file)
            is_load = upload_table(csv_file.name)
            if is_load == 'IndexError':
                return HttpResponse('<h1>Колличество столбцов в файле не соответсвует БД!</h1>')
            
            return redirect(reverse('index'))
        else:
            return HttpResponse('<h1>Файл не выбран!</h1>')





