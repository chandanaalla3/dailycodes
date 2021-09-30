'''Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, 
and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.'''

s = input()
s = s.lower()
s1 = list(set(s))
l1 = []
for i in s1:
    l1.append(s.count(i))
res = max(set(l1), key = l1.count) 
j = 0
for i in l1:
    if i > res:
        j += abs(res-i)
    elif i<res:
        j+=1
if j == 1 or j == 0:
    print("YES")
else:
    print("NO")
