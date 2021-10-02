#Given N,  reverse the digits of N.
n = int(input())
sum1 = 0
while n != 0:
    sum1 = sum1 * 10 + (n % 10)
    n = n // 10
print(sum1)
