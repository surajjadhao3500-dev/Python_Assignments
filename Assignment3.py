# Program to find the greatest of three numbers

print("Question-1")
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))

if a >= b and a >= c:
    print("Greatest number is =", a)
elif b >= a and b >= c:
    print("Greatest number is =", b)
else:
    print("Greatest number is =", c)

# Program to check if a number is even or odd

print("Question-2")
num = int(input("Enter a number = "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# Program to check if a character is an uppercase alphabet, lowercase alphabet, or not an alphabet

print("Question-3")
ch = input("Enter a character = ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase Alphabet")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase Alphabet")
else:
    print("Not an Alphabet")

# Program to check if the input is a number or a character  

print("Question-4")
value = input("Enter any value = ")

if value.isdigit():
    print("The input is a Number")
else:
    print("The input is a Character")