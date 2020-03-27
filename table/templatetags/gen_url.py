from django import template
import re


register = template.Library()

@register.filter()
def get_url(request, var):
    full_path = request.build_absolute_uri()

    #http://176.57.215.48:5001/?model_dvs=czc&link=&price_min=&price_max=&price_2_min=&price_2_max=&firm=&drive_unit=&transmission=%D0%92%D1%81%D0%B5&volume=%D0%92%D1%81%D0%B5&fuel=%D0%92%D1%81%D0%B5&name=&information=&number_oem=&number_dvs=&analog=&vin_code=&price_min=35233&price_max=35233
    # full_path = full_path.split('?')
    # parms = full_path[1]
    if '&price_max=' in full_path:
        full_path = re.sub(r'&price_max=', f'&price_max={var}', full_path)
        full_path = re.sub(r'&price_min=', f'&price_min={var}', full_path)
        # full_path = re.sub(r'&price_2_max=', f'&price_2_max={var}', full_path)
        # full_path = re.sub(r'&price_2_min=', f'&price_2_min={var}', full_path)
        full_path = re.sub(r'&price_min=\d+', f'&price_min={var}', full_path)
        full_path = re.sub(r'&price_max=\d+', f'&price_max={var}', full_path)
        # full_path = re.sub(r'&price_2_min=\d+', f'&price_2_min={var}', full_path)
        # full_path = re.sub(r'&price_2_max=\d+', f'&price_2_max={var}', full_path)
    else:
        full_path = full_path +f'&price_min={var}&price_max={var}'


    return full_path

