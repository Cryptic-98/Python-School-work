myTuple = [(2, 3), (4, 6), (5, 2), (8, 4)]


def sort_by_second_element(myTuple):
    myTupleLen = len(myTuple)
    for x in range(myTupleLen):
        for y in range(0, myTupleLen - x - 1):
            if myTuple[y][1] > myTuple[y + 1][1]:
                myTuple[y], myTuple[y + 1] = myTuple[y + 1], myTuple[y]
    return myTuple


sorted_list = sort_by_second_element(myTuple)
print(sorted_list)
