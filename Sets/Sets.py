"""
# is it a set?
mySet = {}
print(type(mySet))

# creating a set
mySet = {3, 7, 7, 9, 9, 4, 5}
mySet2 = set([5, 8, 9, 47])
print(mySet)
# adding elements to a set
mySet.add(78)
print(mySet)
# adding multiple elements
list1 = [23, 89, 100]
mySet.update(list1)
print(mySet)
# removing elements from a set
mySet.remove(89)
print(mySet)
# iterating a set using a loop

# finding a max or min using a loop
setList = list(mySet)
maxValue = setList[0]
minValue = setList[0]
for value in mySet:
    if value < maxValue:
        maxValue = value
    if value > minValue:
        minValue = value 
print(f'Maximum value: {maxValue} and minimum value: {minValue}')
"""
# unionizing sets
setA = {54, 76, 23, 78, 18}
setB = {45, 98, 54, 18, 20}
setC = setA.union(setB)
print(setC)
# intersection of sets
setD = setA.intersection(setB)
print(setD)
#print(help(setC))
dicti = {'r' : 000}
#print(help(dicti))
