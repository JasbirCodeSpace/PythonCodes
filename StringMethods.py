"""
len() and str() practice:
1.create a variable and assign it the string "Python"
2.create another variable and assign it the length of the string assigned to the variable in step 1
3.create a variable and use string slicing and len() to assign it the length of the slice "yth" from the string assigned
 to the variable from step 1
4.create a variable and assign it the float 1.32
5.create a variable and assign it the string "2" from the float assigned to the variable from the last problem (use the
 str() string method for this)
"""

str1 = "Python"
length = len(str1)
print("\n", length)
slice_length = len(str1[1:4])
print("\n", slice_length)

float1 = 1.32
str1 = str(float1)[3]
print("\n", str1)

"""
.upper() and .lower() practice:
1.create a variable and assign it the string "upper" changed to "UPPER" using .upper()
2.create a variable and assign it the string "owe" from "LOWER" using string slicing and .lower()
"""
str1 = "upper".upper()
print("\n", str1)
str2 = "LOWER"[1:4].lower()
print("\n",str2)
