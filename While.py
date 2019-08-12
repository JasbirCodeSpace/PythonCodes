"""
1.While Loop Basics
a.create a while loop that prints out a string 5 times (should not use a break statement)
b.create a while loop that appends 1, 2, and 3 to an empty string and prints that string
c.print the list you created in step 1.b.
2.while/else and break statements
a.create a while loop that does the same thing as the the while loop you created in step 1.a. but uses a break
statement
 to end the loop instead of what was used in step 1.a.
b.use the input function to make the user of the program guess your favorite fruit
c.create a while/else loop that continues to prompt the user to guess what your favorite fruit is until they guess
 correctly (use the input function for this.) The else should be triggered when the user correctly guesses your
 favorite fruit. When the else is triggered, it should output a message saying that the user has correctly guessed
 your favorite fruit.
"""
counter=0
while counter<5:
    print("Hello")
    counter+=1

string = ""
counter =1
while counter<4:
    string +=str(counter)
    counter+=1

print(string)

counter=0
while True:
    print("hello")
    counter +=1
    if counter==5:
        break

def input_fruit():
    return input("Fruit name : ")

fruit = input_fruit()
while fruit!="Apple":
    fruit = input_fruit()
else:
    print("user has correctly guessed favorite fruit : %s"%(fruit))

