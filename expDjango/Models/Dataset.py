from django.db import models

class Dataset(models.Model):
    #BY OMISSION DJANGO POSTGRES CREATE TABLE PUT ID ATTRIBUTE
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
