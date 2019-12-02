from django.shortcuts import render
from expDjango.Models import Dataset
from expDjango.Forms import *

def listAllDatasets(request):
    shelf = Dataset.Dataset.objects.all()
    return render(request, '/templates/preview.html', {'shelf' : shelf}) #ATRIBUTO SHELF NO TEMPLATE PREVIEW, VAI RECEBER TODOS OS OBJETOS QUE ESTAO NA TABELA DATASET
