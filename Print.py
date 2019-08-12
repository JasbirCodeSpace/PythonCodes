"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""

str1 = "hello" + " world"
print("\n", str1)
num1 = 11
num2 = 38

str2 = str(num1)+str(num2)
print("\n", str2)


"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
 [name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""

restaurant = input("what is your favourite restaurant ? ")
place = input("The name of a place where you wants to visit : ")
name = input("Nick name or first name if you don't have a nickname : ")

str1 = "Your favorite restaurant is %s, you want to visit %s, and your nickname or first name is %s"%(restaurant,place,name)

print(str1)

