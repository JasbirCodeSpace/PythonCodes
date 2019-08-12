"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""

def printString():
    print("function with no parameter")

var = 5

def single(a):
    print(a)

printString()
single(var)

"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""

a=1
b=2
c=3

def differ(a,b):
    print(a-b)

def prod(a,b,c):
    print(a*b*c)

differ(a,b)
prod(a,b,c)

"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""


d = 2.2
e =4.65
f = 5.3

def quot(a,b):
    return a//b

def quot2(a,b,c):
    d = quot(a,b)
    return quot(d,c)

var = quot(e,d)
print(var)

print(quot2(f,e,d))