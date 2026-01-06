print("Welcome to the AI Lab!")

# 2
name=input("enter your name")
roll=input("enter your your roll no")
branch=input("enter your branch")
print(f"name:,{name},roll:,{roll},branch:,{branch}")
print("\n")

# 3
a=float(input("enter first number:"))
b=float(input("enter second number"))
print("Sum=",a+b)
print("Diffrence =",a-b)
print("product =",a*b)
if b!=0:
    print("quotient=",a/b)
else:
    print("quotient=division by zero not allowed")
print("\n")

# 4
c=float(input("enter temperature in celsius:"))
f=(9/5)*c+32
print("temperature in fahrenheit=",f)
print("\n")

# 5
num=int(input("Enter a number:"))
if num%2 ==0:
    print(num,"is even")
else: 
    print(num,"is odd")
print("\n")

# 6
x=float(input("enter first number"))
y=float(input("enter second number"))
z = float(input("Enter third number: "))
print("Largest number is", max(x, y, z))
print("\n")

# 7
N = int(input("Enter a number N: "))
print("First", N, "natural numbers:")
for i in range(1, N + 1):
    print(i, end=" ")
print()
print("\n")

# 8
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "=", fact)
print("\n")

# 9
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    numbers.append(float(input(f"Number {i+1}: ")))

print("List =", numbers)
print("Smallest =", min(numbers))
print("Largest =", max(numbers))
print("\n")

# 10

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

p = int(input("Enter a number to check prime: "))
if is_prime(p):
    print(p, "is a Prime Number")
else:
    print(p, "is Not a Prime Number")
print("\n")


