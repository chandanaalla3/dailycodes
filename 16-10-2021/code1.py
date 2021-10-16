#Given a positive integer, N. Find the factorial of N.
 
n = int(input())
res = 1
for i in range(1,n+1):
    res = res * i
print(res)
