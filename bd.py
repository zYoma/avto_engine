import re
import os
import sys
import django

sys.path.append('/home/zyoma/my-server/home/gafuk/FREELANCE/avto-dvig/app/avto_engine')
os.environ['DJANGO_SETTINGS_MODULE'] = 'avto_engine.settings'
django.setup()
from table.models import Table

def bd_add():
    new_list = []
    with open("bd.txt") as file_handler:
        for line in file_handler:
            new_line = re.sub(r'\t', ':::', line)
            new_line = re.sub(r'https://Поставщик\s', 'https://site.ru/', new_line)
            new_line = re.sub(r"'", '', new_line)
            new_list.append(new_line)

    with open('new_bd.txt', 'w') as f:
        for item in new_list:
            f.write("%s" % item)

#bd_add()


def bd():
    new_list = []
    with open("new_bd.txt") as file_handler:
        for line in file_handler:
            new_line = line.split(':::')

            model_dvs = new_line[0]
            if model_dvs == '':
                model_dvs = None
            link = new_line[1]
            if link == '':
                link = None
            price_without_c = new_line[2]
            if price_without_c == '':
                price_without_c = None
            price_with_c = new_line[3]
            if price_with_c == '':
                price_with_c = None
            currency = new_line[4]
            if currency == '':
                currency = None
            firm = new_line[5]
            if firm == '':
                firm = None
            mark = new_line[6]
            if mark == '':
                mark = None
            model = new_line[7]
            if model == '':
                model = None
            body = new_line[8]
            if body == '':
                body = None
            year = new_line[9]
            year = re.sub(r'\D', '', year)

            if year == '':
                year = None
            drive_unit= new_line[10]
            if drive_unit == '':
                drive_unit = None
            transmission = new_line[11]
            if transmission == '':
                transmission = None
            volume = new_line[12]
            if volume == '':
                volume = None
            horsepower = new_line[13]
            if horsepower == '':
                horsepower = None
            fuel = new_line[14]
            if fuel == '':
                fuel = None
            name = new_line[15]
            if name == '':
                name = None
            information = new_line[16]
            if information == '':
                information = None
            number_dvs = new_line[17]
            if number_dvs == '':
                number_dvs = None
            number_oem= new_line[18]
            if number_oem == '':
                number_oem = None
            analog = new_line[19]
            if analog == '':
                analog = None
            vin_code = new_line[20]
            if vin_code == '':
                vin_code = None

            print(price_without_c)
            print(price_with_c)

            new_obj = Table.objects.create(model_dvs=model_dvs,
                link=link,
                price_without_c=price_without_c,
                price_with_c=price_with_c,
                currency=currency,
                firm=firm,
                mark=mark,
                model=model,
                body=body,
                year=year,
                drive_unit=drive_unit,
                transmission=transmission,
                volume=volume,
                horsepower=horsepower,
                fuel=fuel,
                name=name,
                information=information,
                number_dvs=number_dvs,
                number_oem=number_oem,
                analog=analog,
                vin_code=vin_code


                )


bd()