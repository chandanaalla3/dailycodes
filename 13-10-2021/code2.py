'''Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.
Note:A Palindrome number is a number which stays the same when reversed.Example- 121,131,7 etc.'''

n = int(input())
sum1 = 0
while n != 0:
    sum1 += (n % 10)
    n = n // 10
sum1 = str(sum1)
if sum1[::-1] == sum1:
    print("Yes")
else:
    print("No")
