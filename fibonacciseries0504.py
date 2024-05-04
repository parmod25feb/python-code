# 5. Fibonacci Sequence: Write a function to generate the Fibonacci sequence up to a specified number of terms.
# Date : 05/04/2024
# Author : Parmod Kumar

# Ask user to add any value to print the fibonacci series
mx = eval(input("\nPlease enter a max number to print the fibonacci series : "))

# Function definition
def fibonacci_series(mx):
    a,b=0,1
    c=a+b
    print(f"{a},{b},",end='')
    while  c <= mx :
        print(f"{c},",end='')
        a=b
        b=c
        c=a+b
#Calling the function
fibonacci_series(mx)