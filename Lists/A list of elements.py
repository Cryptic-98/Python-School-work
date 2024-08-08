"""
list1 = [7, 7.8, 'John', 'Peter', 89, 70]
print(list1)
list1.append('Bob')
print(list1)
list1.insert(2, "Alice")
print(list1)
# list1.remove('John')
# list1.insert(3, 'Simon')
list1[3] = 'Simon'
print(list1)

# find the sum of the elements in the list: [3 , 5, 6, 7, 8, 10]
mylist = [3, 5, 6, 7, 8, 10]
sum = 0
for number in mylist:
    sum += number
print(f'The sum of all the numbers in the list is: {sum}')

# Write a program to count the even numbers in the list:
list2 = [10, 21, 32, 43, 54, 65, 76]
count = 0
for number in list2:
    if number % 2 == 0:
        count += 1
print(count)

# Write a program to count the maximum and minimum value in the list:
mylist2 = [37, 67, 23, 89, 45]
maximum = mylist2[0]
minimum = mylist2[0]
for number in mylist2:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
print(f'The maximum number is {maximum} and the minimum number is {minimum}')

# Slicing list [2, 4, 7, 9, 10, 67, 4]
newlist = [2, 4, 7, 9, 10, 67, 4]
print(newlist)
print(newlist[0:3])
print(newlist[1:5])
print(newlist[::-1])

myTuple = (1, 8, 'Royal', 'Peter', 78.9, True)
print(myTuple)
print(len(myTuple))
print(myTuple)
# use a loop to print the elements of a tuple
for values in myTuple:
    print(values)
# finding the maximum and minimum number in (6, 9, 4, 78, 100, 56, 45)
newTuple = (6, 9, 4, 78, 100, 56, 45)
maxMIn = newTuple[0]
minMax = newTuple[0]
for value in newTuple:
    if value < maxMIn:
        maxMIn = value
    if value > minMax:
        minMax = value
print(f'The minimum value is {maxMIn} and the maximum value is {minMax}')

# concatenating tuples
tuple1 = (8, 9, 10)
tuple2 = ('Mangoes', 'Bananas', 'Pineapples')
tuple3 = tuple1 + tuple2
print(tuple3)
tuple2 = tuple1 + tuple2
print(tuple2)
"""
# converting a list into a tuple
tupList = [1, 2, 3, 4]
newTup = tuple(tupList)
print(newTup)
