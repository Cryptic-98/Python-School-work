myList = [5, 8, 96, 105, 65]
maxMin = myList[0]
minMax = myList[0]
for value in myList:
    if value > maxMin:
        maxMin = value
    if value < minMax:
        minMax = value
print(f'Minimum Value: {minMax} \nMaximum Value: {maxMin}')
