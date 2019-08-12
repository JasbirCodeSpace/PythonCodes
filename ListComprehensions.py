"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]
2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""

list1 = [item for item in range(8,-1,-2)]
print(list1)

list2 = [pow(item,item) for item in range(1,5,1)]
print(list2)

list3 = [(item*(item+2)) for item in range(4,7,1)]
print(list3)

list4 = [item for item in range(2,10,1)if item!=5 and item!=6]
print(list4)

list5 = [item for item in range(10,0,-1) if item>=8 or item<=3]
print(list5)

list6 = [item for item in range(1,11,1) if item!=2 and item!=3 and item!=7 and item!=8]
print(list6)