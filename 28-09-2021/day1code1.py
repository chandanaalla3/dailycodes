#Given an array of n distinct elements and a number x, 
#arrange array elements according to the absolute difference with x,
#i. e., an element having minimum difference comes first, and so on. 
n = list(map(int,input().split()))
k = int(input())
d1 = {}
for i in n:
    d1[i] = abs(i-k)
d1 = sorted(d1.items(), key = lambda kv:kv[1])
for i in d1:
    print(i[0],end=" ")
