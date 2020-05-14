from django.contrib import admin
from .models import Dataset, CNNModel
# Register your models here.

admin.site.register(Dataset.Dataset)
admin.site.register(CNNModel.CNNModel)