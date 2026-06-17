t1 = (1, 2, 3)
t2 = (4, 5, 6)

print("Length:", len(t1))
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)
print("Membership:", 2 in t1)

t = ("Python", "Java", "C", "C++", "JavaScript")

print("Index 1:", t[1])
print("Negative Index:", t[-1])
print("Slicing:", t[1:4])

print("Iteration:")
for item in t:
    print(item)

    t = (10, 20, 30)

# Tuples are immutable
# t[0] = 100   # Error

print("Original Tuple:", t)

del t
print("Tuple Deleted")

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

lst = [1, 2, 3]
tup = tuple(lst)

print("Converted Tuple:", tup)