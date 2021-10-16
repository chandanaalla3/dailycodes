#Given an array of N positive integers, find GCD of all the array elements.

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
n = int(input())
l = list(map(int,input().split()))
res = l[0]
for i in range(1,n):
    res = gcd(res,l[i])
print(res)
