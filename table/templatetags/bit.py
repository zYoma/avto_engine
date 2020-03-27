from django import template
import re


register = template.Library()

@register.filter()
def get_bit_depth(var):
    var = str(var)
    if len(var) == 4:
        var = re.sub(r'(.)(...)', r'\g<1> \g<2>', var)
    elif len(var) == 5 :
        var = re.sub(r'(..)(...)', r'\g<1> \g<2>', var)
    elif len(var) == 6 :
        var = re.sub(r'(...)(...)', r'\g<1> \g<2>', var)
    elif len(var) == 7:
        var = re.sub(r'(.)(...)(...)', r'\g<1> \g<2> \g<3>', var)
    elif len(var) == 8:
        var = re.sub(r'(..)(...)(...)', r'\g<1> \g<2> \g<3>', var)
    elif len(var) == 9:
        var = re.sub(r'(...)(...)(...)', r'\g<1> \g<2> \g<3>', var)
    elif len(var) == 10:
        var = re.sub(r'(.)(...)(...)(...)', r'\g<1> \g<2> \g<3> \g<4>', var)

    return var
