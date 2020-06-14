from django.db import models
from users.models import CustomUser
from datasets.models import Dataset
from modelos.models import CNNModel

class History(models.Model):
    user_id = models.ForeignKey(CustomUser.CustomUser, on_delete=models.CASCADE)
    dataset_id = models.ForeignKey(Dataset.Dataset, on_delete=models.CASCADE)
    model_id = models.ForeignKey(CNNModel.CNNModel, on_delete=models.CASCADE)
