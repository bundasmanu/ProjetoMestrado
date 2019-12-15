from django.shortcuts import render, redirect
from Dataset.models import Dataset
from Dataset.Forms.DatasetForm import DatasetTemp

def listAllDatasets(request):
    shelf = Dataset.objects.all()
    return render(request, 'dataset/index.html', {'shelf' : shelf}) #ATRIBUTO SHELF NO TEMPLATE PREVIEW, VAI RECEBER TODOS OS OBJETOS QUE ESTAO NA TABELA DATASET

def listDataset(request, idDataset):

    try:

        #CONVERT ID DATASET TO INT --> URL PARAMETER IS A STRING
        idDset = int(idDataset)

        dset = getDataset(idDataset)

        #dsetForm = DatasetTemp(instance=dset) #OBJETO DATASET COM TODOS OS CAMPOS

        return render(request, 'dataset/listDataset.html', {'dset': dset})

    except:
        raise


def getDataset(idDataset):

    '''

    :param idDataset: int id  --> dataset
    :return: dataset object
    '''

    try:

        datasetObject = Dataset.objects.get(id=idDataset)

        if datasetObject == None:
            raise Dataset.DoesNotExist

        return datasetObject

    except:
        raise