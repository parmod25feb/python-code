# 9. Count Vowels and Consonants: Write a function to count the number of vowels and consonants in a given string.
# Date : 06 May, 2024
# Author : Parmod Kumar

st = input("Please enter the string : ")

def count_vowels_and_consonants(st):
    vo,co=0,0
    ls=['a','e','i','o','u','A','E','I','O','U']
    v=[]
    c=[]
    for ch in st: 
        if ch in ls:
            vo += 1
            v.append(ch)
        else: 
            co += 1
            c.append(ch)
    return vo,v,co,c

res = count_vowels_and_consonants(st)
print(f"In the given string : \"{st}\" \n Vowels count is :{res[0]} {res[1]}\n Consonantas count is : {res[2]} {res[3]}\n")