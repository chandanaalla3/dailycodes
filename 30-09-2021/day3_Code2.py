'''Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating 
score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. 
If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.
Example:
arr = [4,6,4,5,6,2]
She gives the students candy in the following minimal amounts: [1,2,1,2,3,1]. She must buy a minimum of 10 candies.'''

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
candies = [1]*n
for i in range(1,n):
    if l[i] > l[i-1]:
        candies[i] = candies[i-1] + 1
for i in range(n-2,-1,-1):
    if l[i] > l[i+1]:
        candies[i] = max(candies[i+1]+1,candies[i])
#print(candies)
print(sum(candies))
