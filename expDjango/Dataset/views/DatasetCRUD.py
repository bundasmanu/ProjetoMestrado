from django.shortcuts import render, redirect
from expDjango.Dataset.Models import Dataset
from expDjango.Dataset.Forms.DatasetForm import DatasetTemp

def listAllDatasets(request):
    shelf = Dataset.Dataset.objects.all()
    return render(request, 'index.html', {'shelf' : shelf}) #ATRIBUTO SHELF NO TEMPLATE PREVIEW, VAI RECEBER TODOS OS OBJETOS QUE ESTAO NA TABELA DATASET

def listDataset(request, idDataset):

    try:

        #CONVERT ID DATASET TO INT --> URL PARAMETER IS A STRING
        idDset = int(idDataset)

        #GET DATASET--> FROM MY DB
        dset = None
        try:
            dset = Dataset.Dataset.objects.get(id=idDset)
        except Dataset.Dataset.DoesNotExist:
            return redirect('index.html') #RETORNA À PÁGINA DE LISTAGEM DOS DATASETS

        #dsetForm = DatasetTemp(instance=dset) #OBJETO DATASET COM TODOS OS CAMPOS

        return render(request, 'listDataset.html', {'dset': dset})

    except:
        raise