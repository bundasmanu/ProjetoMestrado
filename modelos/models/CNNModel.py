from django.db import models
from datasets.models import Dataset
from users.models import CustomUser

class CNNModel(models.Model):
    name = models.CharField(max_length=100, default=None, null=False)
    normalize_mean = models.FloatField(null=False, default=None)
    normalize_std = models.FloatField(null=False, default=None)
    creation_date = models.DateField(auto_now_add=True, blank=True, null=False)
    output_dict = models.CharField(max_length=2500, default={"Enter a valid dictionary"}, null=False, error_messages={'required': 'Please pass a dictionary in this format: {"class1": 0, "class2" : 1}'})
    model_path = models.CharField(max_length=500, default=None, null=False)
    dataset_id = models.ForeignKey(Dataset.Dataset, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser.CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "\nModel Name: {},\tPath of Model: {} and\tName Dataset: {}"\
            .format(self.name, self.model_path, self.dataset_id.name)


# from django.db import models
# from datasets.models import Dataset
#
# class CNNModel(models.Model):
#     name = models.CharField(max_length=100, default=None, null=False)
#     path = models.CharField(max_length=500, default=None, null=False)
#     dataset_id = models.ForeignKey(Dataset.Dataset, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "\nModel Name: {},\tPath of Model: {} and\tName Dataset: {}"\
#             .format(self.name, self.path, self.dataset_id.name)