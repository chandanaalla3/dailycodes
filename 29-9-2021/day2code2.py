#Subarray Division

n = int(input())
cho_bar = list(map(int,input().split()))
day,month = map(int,input().split())
count = 0
for i in range(n):
    x = cho_bar[i:month+i]
    if sum(x) == day:
        count += 1
print(count)
