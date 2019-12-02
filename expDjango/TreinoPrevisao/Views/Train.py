from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

def train(gammaValue, dropdownValue, xTrain, yTrain):

    try:

        #GET MY SVM MODEL --> AND INITIALIZE WITH GAMMA VALUE FROM USER TEXTBOX
        svmModel = svm.SVC(gamma=gammaValue)

        #TRAIN MODEL
        svmModel.fit(xTrain, yTrain)

        return svmModel
    except:
        raise("Something wrong appened")
