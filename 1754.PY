# Introductory Problems : Coin Piles
#  https://cses.fi/problemset/task/1754/

# Solve and obtain 2 equations.

for _ in range(int(input())):
    a, b = map(int, input().split())
    if (2*a - b)%3==0 and (2*a - b)>=0 and (2*b - a)%3==0 and (2*b - a)>=0:
        print('YES')
    else:
        print('NO')
        