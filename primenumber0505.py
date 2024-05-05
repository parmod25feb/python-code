# 6. Check Prime: Write a function to check if a given number is prime.
# Date : 05 May, 2024
# Author : Parmod Kumar

mx = eval(input("\nPlease enter the max range to print the list of prime numbes : "))

def primenumber_check(mx):
    ls =[]
    if mx == 0 or mx == 1:
        print("Not a prime number")
    else:
        for num in range(2,mx):
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                ls.append(num)
    print(ls)

primenumber_check(mx)