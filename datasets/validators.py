import os
from django.core.exceptions import ValidationError

# validator to check if image upload file, has as its extension: .png, .jpeg, .jpg, .jpe .svg, .tiff, .tif, .bmp, .dib, .webp
def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpeg', '.jpg', '.jpe', '.svg', '.tiff', '.tif', '.bmp', '.dib', '.webp']
    if not ext.lower() in valid_extensions:
        print("Validation error")
        raise ValidationError('Unsupported file extension.')