import re
import traceback
from django.contrib import messages
from .config import DATASCIENTIST_GROUP, HEALTH_CARE_GROUP

def func(var):
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
    return vars_name

def getNameGroup(charGroup):
    try:
        if charGroup == "A":
            return "Admin"
        elif charGroup == "D":
            return DATASCIENTIST_GROUP
        elif charGroup == "H":
            return HEALTH_CARE_GROUP
        else:
            return None
    except:
        raise