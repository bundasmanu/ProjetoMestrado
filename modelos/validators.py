import os
from django.core.exceptions import ValidationError
import ast

# validator to check if model upload file, has as its extension: .h5
def validate_model_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.h5']
    if not ext.lower() in valid_extensions:
        print("Validation error")
        raise ValidationError('Unsupported file extension.')

#https://stackoverflow.com/questions/13675942/converting-string-to-dict
def check_output_dict(value):

    try:
        mydict = ast.literal_eval(value)
        if not isinstance(mydict, dict):
            raise
        for value in mydict.values(): # all values need to be integer
            if isinstance(value, int):
                continue
            else:
                if not value.isdigit():
                    raise
    except:
        raise ValidationError('Please give a dictionary')

def check_output_tuple(value):

    try:
        number_commas = value.count(',') # only accepts strings of format 50, 50, 3
        if number_commas != 2:
            raise
        res = tuple(map(int, value.split(', ')))
    except:
        raise ValidationError('Please give a tuple string format')