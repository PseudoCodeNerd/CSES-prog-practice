# https://cses.fi/problemset/task/1755
# Palindrome Reorder

from math import floor
from collections import Counter
s = str(input())
occur = Counter(s)
odd_occur = 0
for k in occur.keys():
    if occur[k]%2!=0:
        odd_occur+=1
        oddChr = k
if odd_occur > 1 or odd_occur == 1 and len(s)%2==0:
    print("NO SOLUTION")
h1, h2 = [], []
for k in occur.keys():
    st = k*(floor(occur[k]/2))
    h1.append(st)
    h2.insert(0, st)
if odd_occur == 1:
    print(''.join(h1)+oddChr+''.join(h2))
else:
    print(''.join(h1)+''.join(h2))