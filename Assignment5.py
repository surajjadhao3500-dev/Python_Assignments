# 1. WAP to Calculate length of string

str1 = input("Enter a string: ")

length = len(str1)
print("Length of string is:", length)


# 2. WAP to make string from 1st two and last two characters from given string

str1 = input("Enter a string: ")

if len(str1) < 2:
    print("String is too short")
else:
    result = str1[:2] + str1[-2:]
    print("New string is:", result)


# 3. WAP to concatenate two strings by python

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2

print("Concatenated string is:", result)