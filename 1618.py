# Introductory Problems : Bit Strings
#  https://cses.fi/problemset/task/1617/

# GIF of powers of 5

n=int(input())
i, c = 5, 0
while n/i >= 1:
    c+=int(n/i)
    i*=5
print(int(c))