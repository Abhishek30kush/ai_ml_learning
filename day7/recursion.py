# def countdown(n):
#     if n <= 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(5)

# Factorial of a number

# factorial of n = n*(n-1)*(n-2)*...*1

# def factorial(n):
#     if n == 0 or n==1: #Base Case
#         return 1
#     else:
#         return n * factorial(n - 1) #Recursive Call
# print(factorial(5)) #Output: 120
# factorial(5) 
# =5*factorial(4)
# =5*4*factorial(3)
# =5*4*3*factorial(2)
# =5*4*3*2*factorial(1)
# =5*4*3*2*1  

#Fibonacci Series 
# Each number is sum of previous two numbers

# def fibonacci(n):
#     if n<=1:    #Base Case
#         return n
#     return fibonacci(n-1) + fibonacci(n-2) #Recursive Call

# # print(fibonacci(6)) 
# 0 1 1 2 3 5 8

# def infinite():
#     print("This function will run forever!")
#     infinite()
# infinite()

# Recursion with lists 
# Caclulate the sum of all elements in a list.
# def sum_list(numbers):
#     if len(numbers)==0: #base case
#         return 0
#     else:
#         return numbers[0] + sum_list(numbers[1:])

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(sum_list(numbers)) #Output: 28


# Find the maximum value in a list. 

# def findMax(numbers):
#     if len(numbers) == 1: #base case
#         return numbers[0]
#     else:
#         max_of_rest = findMax(numbers[1:]) 
#         return numbers[0] if numbers [0] > max_of_rest else max_of_rest
# numbers = [3, 1, 4, 1, 5, 9, 2]
# print(findMax(numbers)) #Output: 9