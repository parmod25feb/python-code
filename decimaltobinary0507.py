# 11. Decimal to Binary Conversion: Write a function to convert a decimal number to its binary equivalent.
# Date : 07 May, 2024
# Author : Parmod Kumar

# Function to convert a decimal number to a binary
def decimal_to_binary(num):
    rem=0
    ls=[]
    while num !=0:
        rem = num%2
        ls.append(str(rem))
        num = num//2
    st = ''.join(reversed(ls)) # Reverse the list before joining
    return st

# Let's run the loop until user cancels it
flag = True
while flag:
    num = int(input("Please enter a decimal number : "))
    result = decimal_to_binary(num)
    print(f"\n{num} is equivalent to binary : {result}")
    ch = int(input("\nPress 1 to continue and 0 to exit : "))
    if ch == 1:
        flag=True
    else:
        flag=False