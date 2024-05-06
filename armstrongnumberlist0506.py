# 7. Armstrong Number: Write a function to check if a given number is an Armstrong number.
# Date : 06 May, 2024
# Author : Parmod Kumar

def armstrong_num_check(mx):
    print(f"\n Here is the list of arm strong numbers < {mx} : ", end='')
    for num in range(1,mx):
        nm=num
        rem,total=0,0
        while num != 0:
            rem = num%10
            total = total + pow(rem,3)
            num= num//10
        if total== nm:
            print(f"{nm},",end='')

flag = True
while flag:
    num = int(input("\nPlease enter your max value to print the list of Armstrong number : "))
    armstrong_num_check(num)
    ch = int(input("\nPress 1 to conitinue\nPress 0 to exit : "))
    if ch:
        flag = True
    else: 
        flag = False
    

