'''Given the first 2 terms A1 and A2 of an Arithmetic Series.
Find the Nth term of the series. '''
a1 = int(input())
a2 = int(input())
n = int(input())
diff = a2 - a1
print(a1 + (n - 1)* diff)
