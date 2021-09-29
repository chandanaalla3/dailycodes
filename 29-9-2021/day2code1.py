#Mini-Max sum

l=list(map(int,input().split()))
max1=l[0]
min1=pow(10,10)
for i in range(len(l)):
    sum1=sum(l)-l[i]
    if sum1>max1:
        max1=sum1
    if sum1<min1:
        min1=sum1
print(min1,max1,sep=" ",end=" ")
