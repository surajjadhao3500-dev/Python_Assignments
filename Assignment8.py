d = {'a': 30, 'b': 10, 'c': 20}

asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", asc)
print("Descending:", desc)

d = {"name": "Suraj", "age": 19}

key = "age"

if key in d:
    print("Key exists")
else:
    print("Key does not exist")

    d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)

print("Merged Dictionary:", d1)

t = (1, 2, 3)

t = t + (4,)

print("Updated Tuple:", t)

t = (10, "Python", 3.14, True)

print("Tuple:", t)

lst = [10, 20, 30, 40, 50]

print("Sum:", sum(lst))

lst = [15, 40, 10, 75, 25]

print("Largest Number:", max(lst))
s = {1, 2, 3}

s.add(4)
s.update([5, 6])

print("Updated Set:", s)

arr = [10, 20, 30, 40, 50]

print("Array:", arr)

print("First Element:", arr[0])
print("Second Element:", arr[1])
print("Third Element:", arr[2])
print("Fourth Element:", arr[3])
print("Fifth Element:", arr[4])