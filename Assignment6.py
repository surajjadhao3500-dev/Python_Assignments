#1. Write a Python program to create a list and demonstrate membership operators (in, not in) to check element presence. 
l=[1, 2, 3, 4, 5]
print(3 in l)
print(6 in l)
print(3 not in l)
print(6 not in l)

#2. Write a program to perform indexing, negative indexing, and slicing operations on a given list. 
l=[1, 2, 3, 4, 5]
print(l[0])
print(l[-1])
print(l[4])
print(l[1:3])

#3.  Write a Python program to update, append, insert, and delete elements from a list using built-in methods. 
l=[1, 2, 3, 4, 5]
l[0]=10
l.append(6)
l.insert(2, 20)
l.remove(4)
print(l)

#4. Write a program to demonstrate basic list operations like concatenation, repetition, length, maximum, and minimum functions. 
l1=[1, 2, 3]
l2=[4, 5, 6]
print(l1+l2)
print(l1*2)
print(len(l1))
print(max(l1))
print(min(l1))
