#Given two numbers A and B, find Kth digit from right of AB.

n1 = int(input())
n2 = int(input())
k = int(input())
print(str(n1 ** n2)[-k])
