def less(a, b):
    return a < b

def more(a, b):
    return a > b

# Copied from timm's dotninja stats.py
def a12slow(lst1,lst2):
    more = same = 0.0
    for x in sorted(lst1):
        for y in sorted(lst2):
            if   x==y :
                same += 1
            elif x > y :
                more += 1
    return (more + 0.5*same) / (len(lst1)*len(lst2))

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
