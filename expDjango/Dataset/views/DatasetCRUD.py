from django.shortcuts import render
from expDjango.Dataset.Models import Dataset
from expDjango.Dataset.Forms import *

def listAllDatasets(request):
    shelf = Dataset.Dataset.objects.all()
    return render(request, 'index.html', {'shelf' : shelf}) #ATRIBUTO SHELF NO TEMPLATE PREVIEW, VAI RECEBER TODOS OS OBJETOS QUE ESTAO NA TABELA DATASET
