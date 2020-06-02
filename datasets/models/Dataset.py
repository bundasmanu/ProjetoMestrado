from django.db import models
from users.models import CustomUser

class Dataset(models.Model):
    name = models.CharField(max_length=100, null=False)
    n_classes = models.IntegerField(null=False, default=None)
    n_samples = models.IntegerField(null=False, default=None)
    dataset_path = models.CharField(max_length=500, null=False)
    link_info = models.URLField(max_length=2000, null=True)
    creation_date = models.DateField(auto_now_add=True, blank=True, null=False)
    user_id = models.ForeignKey(CustomUser.CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "\nName: {}\tNº Classes: {}\tNº Samples: {}".format(self.name, self.n_classes, self.n_samples)

# from django.db import models
# from django.db.models import Count
#
# class Dataset(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     normalize_mean = models.FloatField(null=False, default=None)
#     normalize_std = models.FloatField(null=False, default=None)
#
#     def __str__(self):
#         return "\nName: {}\tTrain Mean: {}\tTrain Std: {}".format(self.name, self.normalize_mean, self.normalize_std)