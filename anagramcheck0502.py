# 3. Anagram Check: Write a function to check if two given strings are anagrams of each other.
# Date : 05/02/2024
# Author : Parmod Kumar

str1 = "abcd"
str2 = "DBca"

def anagram_check(st1, st2):
    if len(st1) != len(st2):
        return False
    else:
        s1 = st1.lower()
        s2 = st2.lower()
        sr1 = ''.join(sorted(s1))
        sr2 = ''.join(sorted(s2))
        if sr1 == sr2:
            return True
        else:
            return False

flag = anagram_check(str1, str2)

if flag:
    print(f"\nYahoo! string - {str1} - and -{str2} - are ANAGRAM strings\n")
else:
    print("\nSorry! strings are NOT anagram.\n")