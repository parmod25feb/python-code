# 2. Palindrome Check: Write a function to check if a given string is a palindrome. e.g. abcba = abcba or 121 = 121
# Date : 05/01/2024
# Author : Parmod Kumar


def palindrome_fuction(st):
    rev= ""
    for ch in st:
        rev=ch + rev
    return rev

# program execution will start from this point 
flag = True
while flag:
    st = input("\nPlease enter your string to check if it is palindrome or not : ")
    res = palindrome_fuction(st)
    if st == res:
        print(f"\nYahoo! - {st} is palindrome of - {res}\n")
    else:
        print(f"\nSorry! {st} is NOT a palindrome string\n")

    ch = eval(input("\nPress 1 to continue and anything to exit : "))
    if ch == 1:
        flag = True
    else:
        flag = False
