# Binary to Decimal Conversion: Write a function to convert a binary number to its decimal equivalent.
# Date : 07 May, 2024
# Author : Parmod Kumar

# Function to convert a binary number to a decimal
def binary_to_decimal(num):
    rem,res=0,0
    count =0
    while num !=0:
        rem = num%10
        res = res + (rem * pow(2,count))
        num = num//10
        count += 1
    return res

# Let's run the loop until user cancels it
flag = True
while flag:
    num = int(input("Please enter a binary number : "))
    result = binary_to_decimal(num)
    print(f"\n{num} is equivalent to decimal : {result}")
    ch = int(input("\n Press 1 to continue and 0 to exit : "))
    if ch:
        flag=True
    else:
        flag=False