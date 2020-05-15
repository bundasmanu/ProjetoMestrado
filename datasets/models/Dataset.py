from django.db import models
from django.db.models import Count

class Dataset(models.Model):
    name = models.CharField(max_length=100, null=False)
    normalize_mean = models.FloatField(null=False, default=None)
    normalize_std = models.FloatField(null=False, default=None)

    def __str__(self):
        return "\nName: {}\tTrain Mean: {}\tTrain Std: {}".format(self.name, self.normalize_mean, self.normalize_std)