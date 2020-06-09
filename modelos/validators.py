import os
from django.core.exceptions import ValidationError

# validator to check if model upload file, has as its extension: .h5
def validate_model_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.h5']
    if not ext.lower() in valid_extensions:
        print("Validation error")
        raise ValidationError('Unsupported file extension.')