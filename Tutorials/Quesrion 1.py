myList = [5, 8, 200, 52, 155]
second_largest = myList[0]
for x in myList:
    for y in myList:
        if x > y and y < x:
            second_largest = y
print(f'The second largest value is {second_largest}')
