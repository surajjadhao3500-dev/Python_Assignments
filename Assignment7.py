#Write a Python program to create a tuple and perform basic operations like length, concatenation, repetition, and membership.
t=(1, 2, 3, 4, 5)
print("Length:", len(t))
print("Concatenation of tuple with (6, 7):", t + (6, 7))
print("Repetition:", t * 2)
print("Membership check:", 3 in t)

#Write a program to demonstrate indexing, negative indexing, slicing, and iteration on a tuple.   
t=(1, 2, 3, 4, 5)
print("Indexing:", t[2])
print("Negative Indexing:", t[-1])
print("Slicing:", t[1:4])
print("Iteration:")
for i in t:
    print(i)

#Write a Python program to show that tuples are immutable and demonstrate tuple deletion using del.  
t=(1, 2, 3, 4, 5)
t[0] = 10  # This will raise an error because tuples are immutable
print(t)
del t  # This will delete the entire tuple
print(t)

#Write a program to apply built-in tuple functions like len(), max(), min(), and tuple() on a given sequence. 
l=[1, 2, 3, 4, 5]
t=tuple(l)
print("Tuple:", t)
print("Length:", len(t))
print("Max:", max(t))
print("Min:", min(t))
