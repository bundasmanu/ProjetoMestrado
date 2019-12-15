import treinoPrevisao.Forms.trainPredForm as tpForm
import expDjango.utils as ut
from django.shortcuts import render_to_response,render, HttpResponseRedirect
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from Dataset.models import Dataset
from Dataset.views import DatasetCRUD
import os

def uploadTrainPredict(request):

    try:

        if request.method == 'POST': #IF FORM HAS BEEN SUBMITTED

            #GET MY FORM WITH PARAMETERS THAT I NEED TO PREVIEW AND PREDICT
            upload = tpForm.TrainPredForm(request.POST, request.FILES) #DATA SHOULD BE SEND VIA HTTP POST, MORE SECURE

            #IF ALL DATA IS VALID --> TRAIN AND PREDICT
            if upload.is_valid():

                #GET ALL DATA
                gammaValue = upload.cleaned_data.get("gammaValue") #FLOAT FIELD, DOESN'T NEED TO CONVERT
                dropdDownSelectedValue = int(upload.cleaned_data.get("dropDownDatasets"))#STRING FIELD, I NEED TO CONVERT TO INT

                #CALL PREVIEW (PREVIEW INSIDE CALLS TRAIN)
                accuracyResult = preview(gammaValue=gammaValue, dropdownValue=dropdDownSelectedValue)

                #RENDER TO RESPONSE--> SEND DATA TO NEW TEMPLATE
                return render(request, 'treinoPrevisao/showAccuracy.html', {'accValue' : accuracyResult})
        else:
            #REDIRECT TO SAME PAGE WITH UPGRADED FORM
            form = tpForm.TrainPredForm()
            return render(request,'treinoPrevisao/trainPreview.html', {'form' : form}) #ALTERAR DPS O NOME DA FORM
    except:
        raise

def preview(gammaValue, dropdownValue):

    try:

        #GET DATASET OBJECT
        uploadDataset = DatasetCRUD.getDataset(dropdownValue)

        #GET DATA AND TARGET FROM DATASET
        uploadFile(uploadDataset)

        # LOAD IRIS DATASET
        iris = datasets.load_iris()

        # SPLIT DATA 75% FOR TRAIN AND 25% FOR PREVISIONS
        xTrain, xTest, yTrain, yTest = train_test_split(iris.data, iris.target, test_size=0.25, random_state=42)

        # GET MY TRAINED MODEL
        svm = train(gammaValue, dropdownValue, xTrain, yTrain)

        # APPLY PREDICT
        previsions = svm.predict(xTest)

        # GET ACCURACY OF MY MODEL
        acc = (previsions == yTest).mean()

        # CONVERT FLOAT TO STRING
        accString = repr(acc)  # RETURN CANONICAL STRING OF OBJECT PASSED IN ARGUMENT

        return accString
    except:
        raise ("Something wrong as appened")

def train(gammaValue, dropdownValue, xTrain, yTrain):

    try:

        #GET MY SVM MODEL --> AND INITIALIZE WITH GAMMA VALUE FROM USER TEXTBOX
        svmModel = svm.SVC(gamma=gammaValue)

        #TRAIN MODEL
        svmModel.fit(xTrain, yTrain)

        return svmModel
    except:
        raise("Something wrong appened")

def uploadFile(datasetObject):

    '''

    :param idDatasetToUpload: dataset object to get file from path
    :return: return data and target from dataset
    '''

    try:

        #ACCESS OBJECT BY ATTRIBUTE PATH AND USING OS
        absolutePath = os.path.abspath(datasetObject.path) #GET ABSOLUTE PATH



        return None
    except:
        raise

def extractFile(file):

    '''

    :param file: file in specific format, e.g, .tab
    :return: data and target
    '''

    try:
        

        return None
    except:
        raise