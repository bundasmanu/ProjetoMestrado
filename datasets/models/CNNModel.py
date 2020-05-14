from django.db import models
from . import Dataset

class CNNModel(models.Model):
    name = models.CharField(max_length=100, default=None, null=False)
    path = models.CharField(max_length=500, default=None, null=False)
    dataset_id = models.ForeignKey(Dataset.Dataset, on_delete=models.CASCADE)

    def __str__(self):
        return "\nModel Name: {},\tPath of Model: {} and\tName Dataset: {}"\
            .format(self.name, self.path, self.dataset_id.name)