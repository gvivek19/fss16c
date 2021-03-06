def less(a, b):
    return a < b

def more(a, b):
    return a > b

def showResults(predictions):
    print "\n=== Predictions on test data ===\n"
    print " inst#     actual  predicted error prediction"
    iteratorIndex = 1
    classNumbers = {}
    classNo = 1
    for row in predictions:
        expected = row[0]
        predicted = row[1]

        if expected not in classNumbers:
            classNumbers[expected] = classNo
            classNo += 1
        if predicted not in classNumbers:
            classNumbers[predicted] = classNo
            classNo += 1
        temp1 = str(classNumbers[expected]) + ":" + str(expected)
        temp2 = str(classNumbers[predicted]) + ":" + str(predicted)
        prediction = (expected == predicted)

        print ("{: >6.0f}".format(iteratorIndex) + "{:>21}".format(temp1) + "{: >21}".format(temp2) + "{:>18.0f}".format(prediction))
        iteratorIndex += 1

def median(numbers):
    import numpy
    return numpy.mean(numbers)
    '''
    n = len(numbers)
    numbers = list(numbers)
    numbers = sorted(numbers)
    if n % 2 == 0 :
        return (numbers[(n-1)//2] + numbers[(n+1)//2]) / 2
    else :
        return numbers[n//2]
    '''
