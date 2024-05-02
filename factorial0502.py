# 4. Factorial: Write a function to compute the factorial of a given number.
# Date : 05/02/2024
# Author : Parmod Kumar

# factorial function calculation using recurrison 
def factorial_function(num):
    if num ==0 or num ==1:
        return 1
    else:
        return(num*factorial_function(num-1))

# let's keep asking the user to enter the number to calculate the factorial
flag = True
while flag:
    num =int(input("\nPlease enter your number to calculate the factorial : "))
    fact = factorial_function(num)
    print(f"\nFactorial of number {num} is = {fact}\n")
    n= int(input(f"Press 1 to conitnue and 0 to exit : "))
    if n ==1:
        flag=True
    else:
        flag=False