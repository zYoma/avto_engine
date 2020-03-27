import sys, os, csv
import django
from datetime import datetime

sys.path.append('/home/zyoma/my-server/home/gafuk/FREELANCE/avto-dvig/app/avto_engine')
os.environ['DJANGO_SETTINGS_MODULE'] = 'avto_engine.settings'
django.setup()
from table.models import *


def upload_table(csv_file):
    old_data = Table.objects.all()
    old_data.delete()

    data = csv.reader(open('media/table/' + csv_file, encoding='cp1251'), delimiter = ';')
    # clear_data = []
    # for n, row in enumerate(data):
    #     if n!=0:
    #         if row[2] == '':
    #             row[2] = 0

    #         if row[3] == '':
    #             row[3] = 0

    #         # if row[4] != 'руб' and row[4] != '':
    #         #     try:
    #         #         currency = Rate.objects.get(currency = row[4])
    #         #     except:
    #         #         row[2] = 0
    #         #         row[3] = 0
    #         #     else:
    #         #         row[2] = round(float(row[2]) * currency.currency_rate)
    #         #         row[3] = round(float(row[3]) * currency.currency_rate)


    #         if row[21] == '':
    #             row[21] = 0
    #         if row[22] == '':
    #             row[22] = None
    #         else:
    #             row[22] = datetime.strptime(row[22], '%d.%m.%Y')
    #     clear_data.append(row)


    try:
        obj_list = [
            Table( 
                id = id,
                model_dvs = row[0],
                link = row[1],
                price_without_c = 0 if row[2] == '' else row[2],
                price_with_c = 0 if row[3] == '' else row[3],
                currency = row[4],
                firm = row[5],
                mark = row[6],
                model = row[7],
                body = row[8],
                year = row[9],
                drive_unit = row[10],
                transmission = row[11],
                volume = row[12],
                horsepower = row[13],
                fuel = row[14],
                name = row[15],
                information = row[16],
                number_dvs = row[17],
                number_oem = row[18],
                analog = row[19],
                vin_code = row[20],
                reliability =  0 if row[21] == '' else row[21],
                date_placement = None if row[22] == '' else datetime.strptime(row[22], '%d.%m.%Y')
            )
            for id, row in enumerate(data)
            if id != 0
        ]
    except (IndexError):
        return 'IndexError'

    Table.objects.bulk_create(obj_list)

    return 'ok'
