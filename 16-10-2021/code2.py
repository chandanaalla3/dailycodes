'''Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.'''

def fact(n):
    res  = 1
    for i in range(1,n+1):
        res = res * i
    return res
n = int(input())
r = int(input())
res1 = fact(n)
res2 = fact(n-r)
print(res1//res2)
