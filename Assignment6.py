# 1. Write a Python program to create a list and demonstrate 
# membership operators (in, not in)

my_list = [10, 20, 30, 40, 50]
print("List:", my_list)

num = int(input("Enter element to check: "))

if num in my_list:
    print(num, "is present in the list")
else:
    print(num, "is not present in the list")

if num not in my_list:
    print(num, "is not in the list")
else:
    print(num, "is in the list")


# 2. Write a program to perform indexing, negative indexing,
# and slicing operations on a list

my_list = [1, 2, 3, 4, 5, 6]

print("List:", my_list)

# Indexing
print("Element at index 2:", my_list[2])

# Negative Indexing
print("Last element:", my_list[-1])

# Slicing
print("Elements from index 1 to 4:", my_list[1:5])
print("First three elements:", my_list[:3])
print("Last three elements:", my_list[-3:])


# 3. Write a Python program to update, append, insert,
# and delete elements from a list

my_list = [10, 20, 30, 40]

print("Original List:", my_list)

# Update
my_list[1] = 25
print("After Update:", my_list)

# Append
my_list.append(50)
print("After Append:", my_list)

# Insert
my_list.insert(2, 35)
print("After Insert:", my_list)

# Delete using remove()
my_list.remove(40)
print("After Remove:", my_list)

# Delete using pop()
my_list.pop()
print("After Pop:", my_list)


# 4. Write a program to demonstrate basic list operations

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
print("Concatenation:", list1 + list2)

# Repetition
print("Repetition:", list1 * 2)

# Length
print("Length of list1:", len(list1))

# Maximum
print("Maximum element:", max(list2))

# Minimum
print("Minimum element:", min(list2))