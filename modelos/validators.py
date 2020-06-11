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

def check_output_dict(value):

    try:
        ast.literal_eval(value)
    except:
        raise ValidationError('Please give a dictionary')

def check_output_tuple(value):

    try:
        res = tuple(map(int, value.split(', ')))
    except:
        raise ValidationError('Please give a tuple string format')