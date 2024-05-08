# 12. Find Missing Number: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, write a function to find the one missing from the sequence.
# Date : 08 May, 2024
# Author : Parmod Kumar

ls = [0,1,2,3,4,5,6,7,8]

def missing_number(ls):
    nm=0
    for i in range(0,len(ls)-1):
        if ls[i]+1 != ls[i+1] :
            nm = ls[i]+1
            break
    return nm


res = missing_number(ls)

print(f"\nMissing number is : {res} in the list : {ls}\n")