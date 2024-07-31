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
"""
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
