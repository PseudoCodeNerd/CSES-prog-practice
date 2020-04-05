# Introductory Problems : Increasing Array
#  https://cses.fi/problemset/task/1094/

# to calculate the minimum number of turns, we can just make ever subsequent
# element equal to it's predeccesor. so we need to find out how much is the difference
# b/w a pair of elems and if the successor is bigger, we just make predec equal to it.

n = int(input())
a = list(map(int, input().split()))
s, foo = 0, a[0]
for i in range(1, len(a)):
    if a[i] < foo: s += (foo - a[i])
    else:
        foo = a[i]
print(s)
