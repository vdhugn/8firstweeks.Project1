import re

str1 = str(input())
str2 = str(input())
T = str(input())

def replaceText(str1, str2, T):
    return re.sub(str1, str2, T)

print(replaceText(str1, str2, T))