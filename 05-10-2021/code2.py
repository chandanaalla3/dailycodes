'''An integer d is a divisor of an integer n if the remainder of n/d=0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.'''

for _ in range(int(input())):
    count = 0
    n = input()
    n1 = int(n)
    #print(n)
    for i in n:
        #print(i)
        if i != '0' and n1 % int(i) == 0:
            count += 1
    print(count)
