#Given two numbers A and B. The task is to find out their LCM and GCD
def gcd(a,b):
  if a == 0 :
    return b 
  return gcd(b%a, a)
a = int(input())
b = int(input())
gcd1 = gcd(a,b)
lcm1 = (a * b) // gcd1
print(lcm1,gcd1)
