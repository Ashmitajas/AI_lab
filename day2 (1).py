# Q1) Assign different types of values to variables, print them, show types, and delete a variable
a = 10
b = 3.14
c = "Hello"
d = True
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
del c
# print(c)  # This will cause error because c is deleted


# Q2) Reverse a 3-digit number using operators only
num = int(input("Enter 3-digit number: "))
rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
print("Reversed number:", rev)


# Q3) Input first name and last name and print last name followed by first name
first = input("Enter first name: ")
last = input("Enter last name: ")
print(last + " " + first)


# Q4) Compare memory locations and perform division
x = 10
y = 20
print("Memory location of x:", id(x))
print("Memory location of y:", id(y))
print("Floating division:", x / y)
print("Integer division:", x // y)


# Q5) Find biggest of two numbers using operators only
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
big = (n1 > n2) * n1 + (n2 >= n1) * n2
print("Biggest number:", big)


# Q6) Swap two numbers without 3rd variable using + and -
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a = a + b
b = a - b
a = a - b
print("After swapping:", a, b)


# Q7) Check if element exists in set using operator only
my_set = {1, 2, 3, 4, 5}
ele = int(input("Enter element to search: "))
print(ele in my_set)


# Q8) Check if three numbers can form triangle using operators only
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
result = (a + b > c) and (a + c > b) and (b + c > a)
print(int(result))


# Q9) Distance between two coordinates using operators only
import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance:", dist)


# Q10) Check palindrome 3-digit number without loop
num = int(input("Enter 3-digit number: "))
rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
print("Palindrome" if num == rev else "Not Palindrome")


# Q11) Convert alphabet to opposite case
ch = input("Enter a character: ")
if ch.islower():
    print(ch.upper())
else:
    print(ch.lower())


# Q12) Generate Fibonacci series
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Q13) Find distinct prime factors of a number
num = int(input("Enter number: "))
factors = set()
i = 2
while i <= num:
    if num % i == 0:
        factors.add(i)
        num //= i
    else:
        i += 1
print("Prime factors:", factors)


# Q14) Decimal to Binary/Octal/Hex using match-case
num = int(input("Enter decimal number: "))
print("1) Binary\n2) Octal\n3) Hexadecimal")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Binary:", bin(num))
    case 2:
        print("Octal:", oct(num))
    case 3:
        print("Hexadecimal:", hex(num))
    case _:
        print("Invalid choice")


# Q15) Guessing game
import random
secret = random.randint(1, 100)
guess = 0
while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("Congratulations! You guessed it!")


# Q16) Generate pyramid using nested loop
rows = int(input("Enter number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))
