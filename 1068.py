# Introductory Problems : Weird Algorithm
#  https://cses.fi/problemset/task/1068/

# Basic : Just do as the question says.

n = int(input())
log = []
log.append(n)
while log[-1] != 1:
    if log[-1]%2 == 0:
        log.append(log[-1]//2)
    elif log[-1]%2 == 1:
        log.append((log[-1])*3+1)
res = [str(l) for l in log]
print(' '.join(res))