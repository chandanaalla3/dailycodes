#Given two positive integers A and B, find GCD of A and B.
def gcd(a,b):
  if a == 0 :
    return b 
  return gcd(b%a, a)
n = int(input())
print(gcd(a,b))
