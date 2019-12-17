from sklearn import metrics
from sklearn.metrics import confusion_matrix
import numpy as np

class ConfusionMatrix():

    def __init__(self, yTrue, yPred):
        self.yTrue = yTrue
        self.yPred = yPred

    def getConfusionMatrix(self):
        return confusion_matrix(self.yTrue, self.yPred)

    @property
    def getAccuracy(self):
        return metrics.accuracy_score(self.yTrue, self.yPred)

    @property
    def getPrecision(self):
        return metrics.precision_score(self.yTrue, self.yPred, average='weighted')

    @property
    def getRecall(self):
        return metrics.recall_score(self.yTrue, self.yPred, average='weighted')

    @property
    def getF1Score(self):
        return metrics.f1_score(self.yTrue, self.yPred, average='weighted')