"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""

str1 = "string 1"
str2 = 'str2'
str3 = 'this is a \"quoted\" string'
str4 = 'this is a \'quoted\' string'

print(str1,str2,str3,str4)

"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters.
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.
"""
lannisters = "JaimeCerseiTyrion"

temp = lannisters[1]
print("\n",temp)
temp = lannisters[0]
print("\n",temp)
temp = lannisters[:5]
print("\n",temp)
temp = lannisters[5:11]
print("\n",temp)
temp = lannisters[11:]
print("\n",temp)

