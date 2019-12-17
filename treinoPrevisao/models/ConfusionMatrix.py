
class ConfusionMatrix():

    def __init__(self, accuracy = None, precision = None, recall = None, f1Score = None):
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1Score = f1Score

    @property
    def getAccuracy(self):
        return self.accuracy

    @property
    def getPrecision(self):
        return self.precision

    @property
    def getRecall(self):
        return self.recall

    @property
    def getF1Score(self):
        return self.f1Score