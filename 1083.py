# Introductory Problems : Missing Number
#  https://cses.fi/problemset/task/1083/

# We can obtain missing numbers by finding sum from 1->n and then 
# subtracting the sum of the numbers we have in the list. 

n = int(input())
a = list(map(int, input().split()))
n2 = sum(a)
n1 = (n*(n+1))//2
print(n1-n2)