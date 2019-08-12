"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable
1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input
2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input
3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
 result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.
4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
 .index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""
import random

list1 = [4,2,3,6,1,5,8]
list2 = ["A","B","C","D","E","F","G"]
list3 = [4.2,6.04,2.5,8.1,9.33,1.01,3.0]

def item(x):
    return x

print(item(list1))
print(item(list2))
print(item(list3))

def element(list):
    return list[random.randint(0,len(list)-1)]

print(element(list1))
print(element(list2))
print(element(list3))


def prod(li):
    result =1
    for item in li:
        result*=item
    print("Product = ",result)

prod(list1)

def concat(li):
    result = ""
    for item in li:
        result+=str(item)+" "
    print(result)

concat(list2)

def quotient(list):
    print(list[random.randint(0,len(list)-1)]//list[random.randint(0,len(list)-1)])

quotient(list3)

def three(list):
    list.append(10)
    list.remove(2)
    list.insert(2,11)
    print(list)
three(list1)