#=========================================================================================================
# 1. Write a Python program using nested if-else statements to determine a student’s grade based on marks:
# Marks >= 80: A , Marks >= 60: B,Marks >= 40: C , Marks < 40 : F
#==========================================================================================================
'''Soln'''
Python = P = 80
Calculus = C = 70
Digitology = D = 100
Socilology = S = 50
AI = 80
English = E = 90

Total_marks = P+C+D+S+AI+E
Marks = Total_marks / 6

if P >= 40 and C >= 40 and D >= 40 and S >= 40 and AI >= 40 and E >= 40:
    if Marks >= 80:
        print("Passed....... Grade : A ")
    if 80 > Marks >= 60 :
        print("Passed....... Grade :  B")
    if 60 > Marks >= 40:
        print("Passed....... Grade : C ")
else :
    print("Failed....")


#========================================================================================================
# 2. Write a Python program to find the largest of three numbers entered by the user using if-elif-else.
#========================================================================================================
'''Soln'''
x , y , z = map(int, (input("Enter 3 numbers : ").split()))

if x > y > z :
    print(x,"is the greatest")
elif y > x > z:
    print(y,"is the greatest")
else :
    print(z,"is the greatest")


#==================================================================================
# 3. Write a Python program to check whether a number is prime or not using a loop.
#==================================================================================
'''Soln'''
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")


#=====================================================================================
# 4. Write a Python program to print all even numbers from 1 to 50 using a while loop.
#=====================================================================================
'''Soln'''
i = 1
while i <= 50 :
    if i % 2 == 0 :
        print(i)
    i+=1


#=========================================================================
#5. Write a Python program to check whether a number is palindrome or not.
#=========================================================================
'''Soln'''
x = input("Enter number : ")

reverse = x[::-1]

if x == reverse :
    print(f"The given number {x} is a palindrome number")
else :
    print(f"The given number {x} is not a palindrome number")


#==================================================================================================
# 6. Write a Python program to print the multiplication table from 1 to 10 using a nested for loop.
#==================================================================================================
'''Soln'''
for i in range(1,11):
    print(f"Multiplication table of {i}")
    for j in range(1,11):
        print(f"{i} * {j} =",i*j)


#==================================================================================================
# 7.Write a python program to pring the square pattern
# * * * *
# * * * *
# * * * *
# * * * *
#==================================================================================================
'''Soln'''
num = 4
for i in range(0 , num) :
    for j in range (num):
        print("*" , end="  ")
    print()


#==================================================================================================
# 8. Write a Python program to print a pattern using nested loops:
# *
# * *
# * * *
# * * * *
# * * * * *
#==================================================================================================
'''Soln'''
num = 5 
for i in range(0,num+1):
    for j in range(i):
        print("*", end=" ")
    print()


#==================================================================================================
# 9.Write a Python program to print a following pattern using nested loops:
# * * * * *
# * * * *
# * * *
# * *
# *
#==================================================================================================
'''Soln'''
num = 5 
for i in range(0,num+1):
    for j in range(i,num):
        print("*", end=" ")
    print()


#==================================================================================================
#10.Write a Python program to print a follwing pattern using nested loops:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
#==================================================================================================
'''Soln'''
num = 5
for i in range(1,num+1):
    for j in range(i):
        print(i , end=" ")
    print()


# ====================================================================================================
# 11. Write a Python program to print star pyramid pattern:
#     *b 
#    ***
#   *****
#  *******
# *********
# ===================================================================================================
'''Soln'''
num = 5
for i in range(1 , num+1):
    for j in range(num-i):
        print("", end="  ")
    for k in range(2*i-1):
        print("*", end=" ")
    print() 


#==================================================================================================
# 12 .Write a python program to print following pattern
#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5
# =================================================================================================
'''Soln'''
num = 5
for i in range(1,num+1):
        for j in range(num-i):
                print("", end="   ")
        for k in range(2*i-1):
                print(i, end = "  ")
        print()

        

#==================================================================================================
# 14 . Print the follwing pattern
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# =================================================================================================
'''Soln'''
num = 5 
for i in range(0,num+1):
        for j in range(i):
                print("", end="  ")
        for k in range(num-i):
                print("*", end=" ")
        print()


#==================================================================================================
# 15. Print the following pattern
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# =================================================================================================
'''Soln'''
num = 5 
for i in range(0,num+1):
        for j in range(num-i):
                print("", end="  ")
        for k in range(i):
                print("*", end=" ")
        print()


'''Chapter: 5 Lab Exercise'''

#=====================================================================================================
# 1.Write a Python program to create a function that takes two numbers as parameters and returns
# their sum.
# ====================================================================================================
'''Soln'''
def calc_sum (a , b):
    return(a+b)

sum = calc_sum(7 , 3)
print(sum)


#=====================================================================================================
# 2.Write a function that accepts a number as argument and checks whether it is prime or not.
# ====================================================================================================
'''Soln'''
def num(a):
    if a % 2 == 0 :
        print("Not Prime")
    else:
        print("Prime")

check_Prime = num(2)


#=====================================================================================================
# 3.Write a Python function using assert statement to check that the input number is positive. If not,
# the program should give an error.
# ====================================================================================================
''''Soln'''
value = int(input("Enter a positive number :"))
assert value > 1 , ' The number you gave is negative.'


#=====================================================================================================
# 4.Write a Python program to create a function that accepts a string and returns the number of
# vowels in it.
# ====================================================================================================
'''Soln'''
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1     
    return count
string = input("Enter a string: ")
result = count_vowels(string)
print("Number of vowels:", result)


#=====================================================================================================
# 5.Write a program to demonstrate the use of:Local variable , Global variable
# ====================================================================================================
'''Soln'''
num = 2 # Global Variable
def local_function():
    num1 = 10 # Local Variable
    sum = num + num1 # Accessing global variable in function because it can be possible due to global
    print(sum)
local_function()


#=====================================================================================================
# 6.Write a recursive function to calculate the factorial of a given number.
# ====================================================================================================
'''Soln'''
def fact(n):
    if n == 0 :
        return 1
    return n * fact(n-1)
result = fact(5)
print(result)


#=====================================================================================================
# 7.Write a recursive function to generate the Fibonacci number at position n.
# ====================================================================================================
'''Soln'''
def fib(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return fib(num-1) + fib(num-2)
res=fib(7)
print(res)



#=====================================================================================================
# 8.Write a recursive function to find the sum of digits of a given number.
# ====================================================================================================
'''Soln'''
def num(n):
    if n == 0:
        return 0
    return n%10 +num(int(n/10))

ans = num(1234)
print(ans)



#=====================================================================================================
# 9.Write a recursive function to find the sum of first n natural numbers.
# ====================================================================================================
'''Soln'''
def sum(n):
    return (n * (n+1))/2

number = int(sum(5))
print(number)



#=====================================================================================================
# 10.Write a function to calculate the area of a circle. Take radius as parameter.
# ====================================================================================================
'''Soln'''
def radius(r):
    return 3.14 * r**2

area = radius(4)
print(area)


#=====================================================================================================
# 11.Write a function that takes three numbers and returns the smallest among them.
# ====================================================================================================
'''Soln'''
def input_value(a , b , c):
        if b < a > c :
                print(f"{a} is the greatest.")
        elif a < b > c :
                print(f"{b} is the greatest.")
        else :
                print(f"{c} is the greatest.")

a = input("Enter the first value : ")
b = input("Enter the second value : ")
c = input("Enter the third value : ")

input_value(a,b,c)


#=====================================================================================================
# 12.Write a function that accepts a number and prints its multiplication table.
# ====================================================================================================
'''soln'''
for i in range(1 , 6):
    print("Multiplication table of", i)
    for j in range(1 , 11):
        # print(i, "*" , j , i*j)
        print( f'{i}*{j} =', i*j)



#=====================================================================================================
# 13.Write a recursive function to find LCM of two numbers.
# ====================================================================================================
'''Soln'''
def lcm(a, b):
    if b == 0: 
        return a
    else:
        return lcm(b, a % b)
a = int(input("Enter a natural number:"))
b = int(input("Enter another natural number:"))

result = lcm(a, b)
print("LCM is", result)