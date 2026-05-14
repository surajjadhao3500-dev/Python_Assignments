# Program to display even numbers from 1–10

print("Even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Program to display odd numbers from 1–10

print("Sum of Odd numbers from 1 to 10:")
sum = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum = sum + i
print("Sum of odd numbers:", sum)

# Program to display Fibonacci series up to 50

print("Fibonacci Series up to 50:" )
a = 0
b = 1
print("Fibonacci Series:")

while a <= 50:
    print(a)
    c = a + b
    a = b
    b = c

# Program to remove characters from odd index values in a string

print("String after removing odd index characters:")
text = input("Enter a string: ")
result = text[0::2]
print("String after removing odd index characters:", result)