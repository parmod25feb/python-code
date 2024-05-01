# Reverse a String: Write a function to reverse a given string.
# Date : 05/01/2024
# Author : Parmod Kumar

str1 = input("\n Please enter the string : ")

# Reverse function using the empty string 
def string_reverse(str1):
    rev=""
    for ch in str1:
        rev = ch + rev
    return rev
# Calling the reverse function and the storing the value in the parameter
res_str = string_reverse(str1)

# Printing the reverse of the string 
print(f"\n Method 1 : Reverse of - {str1} is : {res_str}\n")


# Reverse of the string using slicing method
print(f"\n Method 2 : Reverse of - {str1} is : {str1[::-1]}\n")

# we can find the string reverse using the length of the string as well.