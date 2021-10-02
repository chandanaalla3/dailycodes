#Given a Binary Number B, find its decimal equivalent.
str1 = int(input())
sum1 = 0
i = 0
while str1 != 0:
    res = str1 % 10
    sum1 += (res * (2 ** i))
    i += 1
    str1 = str1 // 10
print(sum1)
