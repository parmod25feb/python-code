# 7. Armstrong Number: Write a function to check if a given number is an Armstrong number.
# Date : 06 May, 2024
# Author : Parmod Kumar

def armstrong_num_check(nm):
    rem,total=0,0
    while nm != 0:
        rem = nm%10
        total = total + pow(rem,3)
        nm= nm//10
    return total


flag = True
while flag:
    num = int(input("\nPlease enter your number to check if armstrong or not : "))
    res = armstrong_num_check(num)
    if res == num:
        print(f"Yahoo! {num} is armstrong number.\n")
    else:
        print(f"Sorry! {num} is NOT armstrong number\n")
    ch = int(input("Press 1 to conitinue\nPress 0 to exit : "))
    if ch:
        flag = True
    else: 
        flag = False
    

