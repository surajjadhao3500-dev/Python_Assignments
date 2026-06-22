#1. WAP to display even numbers from 1-10 
for i in range (1,11):
    if i%2==0:
        print(i)

#2. WAP to add odd numbers from 1-10
for i in range (1,11):
    if i%2!=0:
        print(i)

#3. Write a Python program to get the Fibonacci series between 0 to 50. 
a=0
b=1
while a <= 50:
    print(a)
    c=a+b
    a=b
    b=c

#4. Write a Python program to remove the characters which have odd index valuesof a given string.
s="Python"
print(s[::2])
