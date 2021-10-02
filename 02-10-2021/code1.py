#Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M. 
#If there are more than one such number, then output the one having maximum absolute value.

n = int(input())
m = int(input())
q = int( n / m)
x = q * m
if n * m > 0:
    y = m * (q + 1)
else:
    y = m * (q - 1)
if abs(y - n) > abs(x - n):
    print(x)
else:
    print(y)
