from django.shortcuts import render
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from Dataset.views import DatasetCRUD
import os
import pandas as pd
import numpy as np
from treinoPrevisao.Forms import trainPredForm
from treinoPrevisao.models import ConfusionMatrix

def uploadTrainPredict(request):

    try:

        if request.method == 'POST': #IF FORM HAS BEEN SUBMITTED

            #GET MY FORM WITH PARAMETERS THAT I NEED TO PREVIEW AND PREDICT
            upload = trainPredForm.TrainPredForm(request.POST, request.FILES) #DATA SHOULD BE SEND VIA HTTP POST, MORE SECURE

            #IF ALL DATA IS VALID --> TRAIN AND PREDICT
            if upload.is_valid():

                #GET ALL DATA
                gammaValue = upload.cleaned_data.get("gammaValue") #FLOAT FIELD, DOESN'T NEED TO CONVERT
                dropdDownSelectedValue = int(upload.cleaned_data.get("dropDownDatasets"))#STRING FIELD, I NEED TO CONVERT TO INT

                #CALL PREVIEW (PREVIEW INSIDE CALLS TRAIN)
                confusionMat = preview(gammaValue=gammaValue, dropdownValue=dropdDownSelectedValue)

                #RENDER TO RESPONSE--> SEND DATA TO NEW TEMPLATE
                return render(request, 'treinoPrevisao/showAccuracy.html', {'confusionMatrix' : confusionMat})
        else:
            #REDIRECT TO SAME PAGE WITH UPGRADED FORM
            form = trainPredForm.TrainPredForm()
            return render(request,'treinoPrevisao/trainPreview.html', {'form' : form}) #ALTERAR DPS O NOME DA FORM
    except:
        raise

def preview(gammaValue, dropdownValue):

    try:

        #GET DATASET OBJECT
        uploadDataset = DatasetCRUD.getDataset(dropdownValue)

        #GET DATA AND TARGET FROM DATASET
        data, target = uploadFile(uploadDataset)

        # SPLIT DATA 75% FOR TRAIN AND 25% FOR PREVISIONS
        xTrain, xTest, yTrain, yTest = train_test_split(data, target, test_size=0.25, random_state=42)

        # GET MY TRAINED MODEL
        svm = train(gammaValue, dropdownValue, xTrain, yTrain)

        # APPLY PREDICT
        previsions = svm.predict(xTest)

        #RESHAPE PREVISIONS OUTPUT TO FORMAT (1, NUMBER OF SAMPLES)
        previsionsX = previsions.reshape(-1,1)

        # GET ACCURACY, PRECISION, RECALL AND F1_SCORE --> STORE DATA INTO FORM, TO DISPLAY AFTER ON A NEW TEMPLATE
        confusionMat = ConfusionMatrix.ConfusionMatrix()
        confusionMat.accuracy = metrics.accuracy_score(yTest, previsionsX)
        confusionMat.precision = metrics.precision_score(yTest, previsionsX, average='weighted')
        confusionMat.recall = metrics.recall_score(yTest, previsionsX, average='weighted')
        confusionMat.f1Score = metrics.f1_score(yTest, previsionsX, average='weighted')

        return confusionMat
    except:
        raise ("Something wrong as appened")

def train(gammaValue, dropdownValue, xTrain, yTrain):

    try:

        #GET MY SVM MODEL --> AND INITIALIZE WITH GAMMA VALUE FROM USER TEXTBOX
        svmModel = svm.SVC(gamma=gammaValue)

        #TRAIN MODEL
        svmModel.fit(xTrain, np.ravel(yTrain)) #RAVEL USE TO DISABLE WARNING

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

        #EXTRACT FILE
        data, target = extractFile(absolutePath)

        return data, target
    except:
        raise

def extractFile(file):

    '''

    :param file: file in specific format, e.g, .tab
    :return: data and target
    '''

    try:

        #GET DATA FRAMES OBJECT, AFTER READ CSV FILE
        dataset = pd.read_csv(file)

        #CREATE DATAFRAME OBJECT
        df = pd.DataFrame(dataset)

        #RENAME TARGET COLUMN NAME TO CLASS
        df.rename(columns={df.columns[df.shape[1]-1]: 'Class'},inplace=True)

        #GET DATA--> ALL COLUMNS EXCEPT FIRST LINE (ID) AND LAST ONE (TARGET)
        dataDFrame = df[df.columns[1:df.shape[1]-1]]

        #GET TARGET--> LAST COLUMN
        targetDFrame = df[df.columns[df.shape[1]-1]]

        #CONVERT CATEGORICAL COLUMNS OF TARGET TO NUMERIC
        targetDFrameConverted = transformCategoricalTargetIntoInteger(targetDFrame)

        #CONVERT DATAFRAME'S TO NUMPY ARRAY --> SCIKIT LEARN WANTS NUMPY ARRAY
        data = dataDFrame.to_numpy()
        target = targetDFrameConverted.to_numpy()

        return data, target
    except:
        raise

def transformCategoricalTargetIntoInteger(dataframe):

    '''

    :param data: dataframe, columns  to convert
    :return: categorical data converted from categorical to integer
    '''

    try:

        print(dataframe.dtypes)

        #CONVERT SERIES OBJECT TO DATA FRAMES --> TO MAKE ALL ALTERATIONS
        dataframe = dataframe.to_frame()

        #CONVERT TO CATEGORY AND THEN APPLY NUMERIC CONVERSION --> ONLY HAVE ONE COLUMN ON TARGET
        dataframe['Class'] = dataframe['Class'].astype('category')
        cat_columns = dataframe.select_dtypes(['category']).columns
        dataframe[cat_columns] = dataframe[cat_columns].apply(lambda x: x.cat.codes)

        return dataframe
    except:
        raise