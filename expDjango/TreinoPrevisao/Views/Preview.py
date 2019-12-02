from sklearn import datasets
from sklearn.model_selection import train_test_split
from . import Train

def preview(gammaValue, dropdownValue):
    try:
        # LOAD IRIS DATASET
        iris = datasets.load_iris()

        # SPLIT DATA 75% FOR TRAIN AND 25% FOR PREVISIONS
        xTrain, yTrain, xTest, yTest = train_test_split(iris.data, iris.target, test_size=0.25, random_state=42)

        #GET MY TRAINED MODEL
        svm = Train.train(gammaValue, dropdownValue, xTrain, yTrain)

        #APPLY PREDICT
        previsions = svm.predict(xTest)

        #GET ACCURACY OF MY MODEL
        acc = (previsions == yTest).mean()

        #CONVERT FLOAT TO STRING
        accString = repr(acc) #RETURN CANONICAL STRING OF OBJECT PASSED IN ARGUMENT

        return accString
    except:
        raise("Something wrong as appened")
