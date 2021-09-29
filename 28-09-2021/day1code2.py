#Find second largest number in the list
n = list(map(int,input().split()))
n1 = set(n)
n1.remove(max(n1))
if len(n) == 1:
    print("-1")
else:
    print(max(n1))
