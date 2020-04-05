# Introductory Problems : Number Spiral
#  https://cses.fi/problemset/task/1071/

# observe grid, generalize a formula.

for _ in range(int(input())):
    r, c = map(int, input().split())
    if c > r:
        if c%2==0:
            c-=1
            print((c**2+r))
        else:
            print(((c**2)-r+1))
    else:
        # now the formula gets reversed
        if r%2==0:
            print(((r**2)-c+1))
        else:
            r-=1
            print((r**2+c))