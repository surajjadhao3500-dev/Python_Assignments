#1. WAP to find out greatest of 3 numbers 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a,"is greatest")
elif b>a and b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")

#2. WAP to find whether given number is odd or even
n=int(input("Enter a number:"))
if n%2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

#3. Write a C program to check whether a character is uppercase or lowercase alphabet 
ch = input("Enter a character: ")
if ch.isupper():
    print(ch, "is an uppercase alphabet")
else:
    print(ch, "is a lowercase alphabet")

#4. WAP to find whether given input is number or character 
a=input("Enter anything:")
if a.isdigit():
    print(a, "is a number")
else:
    print(a, "is a character")
