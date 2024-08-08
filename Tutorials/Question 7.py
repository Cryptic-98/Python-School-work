myTuple1 = (2, 6, 8)
myTuple2 = (3, 5, 9)
tupleSum = []


def add_tuples(myTuple1, myTuple2):
    for x in range(len(myTuple1)):
        tupleSum.append(myTuple1[x] + myTuple2[x])
    return tuple(tupleSum)


print(add_tuples(myTuple1, myTuple2))
