'''
ADD FRACTIONS
You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).'''
num1 = int(input())
den1 = int(input())
num2 = int(input())
den2 = int(input())
num = num1 * den2 + num2 * den1
den = den1 * den2
res = gcd(num,den)
num = num // res
den = den // res
print(str(num) + '/' + str(den))
    
