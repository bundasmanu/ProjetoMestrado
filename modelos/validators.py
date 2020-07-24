import os
from django.core.exceptions import ValidationError
import ast
import decimal

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
        try:
            mydict = ast.literal_eval(value)
        except:
            raise
        if not isinstance(mydict, dict):
            raise
        for value in mydict.values(): # all values need to be integer
            if isinstance(value, int):
                continue
            else:
                if not value.isdigit():
                    raise
    except:
        raise ValidationError('Invalid dictionary')

def check_output_tuple(value):

    try:
        number_commas = value.count(',') # only accepts strings of format 50, 50, 3
        if number_commas != 2:
            raise
        try:
            res = tuple(map(int, value.split(', ')))
        except:
            raise
    except:
        raise ValidationError('Please give a tuple string format')

def check_output_tuple_normalized_values(value):

    try:
        number_commas = value.count(',') # only accepts strings of format 50.23332, 50.232, 3.22332
        if number_commas not in (0, 2):
            raise
        number_points = value.count('.')
        if number_commas == 0 and number_points == 1: # grayscale image
            res = float(value)
        else: # RGB image
            if number_points == 3:
                try:
                    res = tuple(map(str, value.split(', ')))
                except:
                    raise
            else:
                raise
    except:
        raise ValidationError('Please pass a correct normalized tuple')