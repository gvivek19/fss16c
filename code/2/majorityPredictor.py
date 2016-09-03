import sys

class MajorityPredictor:
    def __init__(self, fileName) :
        self.counts = {}
        self.classNumber = {}
        self.train(fileName)
        self.setMajorityClass()
       
    def train(self, fileName) :
        file = open(fileName)
        dataStarted = False
        for line in file:
            line = line.strip()
            if line == None or line == "":
                continue
            if dataStarted == True :
                classAttribute = line.split(",")[-1]
                existingCount = self.counts.get(classAttribute, 0)
                self.counts[classAttribute] = existingCount + 1
            if line.lower() == "@data":
                dataStarted = True
    
    def setMajorityClass(self) :
        self.prediction = None
        count = -1
        classCount = 0
        for key in self.counts :
            self.classNumber[key] = classCount = classCount + 1
            if self.counts[key] > count :
                count = self.counts[key]
                self.prediction = key
    
    def predict(self, data) :
        predictions = []
        file = open(data)
        dataStarted = False
        for line in file:
            line = line.strip()
            if line == None or line == "":
                continue
            if dataStarted == True :
                predictions.append((line.split(",")[-1], self.prediction))
            if line.lower() == "@data":
                dataStarted = True
        return predictions
        
    def display(self, predictions) :
        print "\n=== Predictions on test data ===\n"
        print " inst#     actual  predicted error prediction"
        
        iteratorIndex = 1
        for item in predictions :
            temp1 = str(self.classNumber[item[0]]) + ":" + item[0]
            temp2 = str(self.classNumber[item[1]]) + ":" + item[1]
            prediction = (item[0] == item[1])
            print ("{: >6.0f}".format(iteratorIndex) + "{:>11}".format(temp1) + "{: >11}".format(temp2) + "{:>8.0f}".format(prediction))
            iteratorIndex += 1
        
if __name__ == '__main__':
    model = MajorityPredictor(sys.argv[1])
    predictions = model.predict(sys.argv[2])
    model.display(predictions)