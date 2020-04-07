# Introductory Problems : Two Sets
#  https://cses.fi/problemset/task/1092/

# Best question attempted in about 3 months.
# we can only divide into two sets if sub till n is divisible into two set.
# looking from the formula of n(n+1)/2 we can see that the series we can get for an 
# equal sum are (n-1, 1), (n-2, 2) ... or (n, 1), (n-1, 2) ...
# first we greedily make the first set then all elems from 1->n not in first set are put in the second set
# and we're done.

n = int(input())
a = [num for num in range(1, n+1)]
s1, curr_sum, px = [], 0, 1
if (n*(n+1))%4!=0: # if not sum not an integer
    print('NO')
    exit
else:
    subset_sum = (n*(n+1))//4
    if subset_sum%n==0:
        s1.append(n)
        curr_sum+=n
    while curr_sum!=subset_sum:
        if subset_sum%n==0:
            # then we take elems (n-1, 1), (n-2, 2) ... to get out half-sum
            s1.append(n - px)
            s1.append(px)
            curr_sum+=n 
        else:
            # when divisible by (n+1)
            s1.append(n - px + 1)
            s1.append(px)
            curr_sum+=(n+1)
        px+=1
    s1.sort(); px = 0; s2 = []
    print('YES')
    print(len(s1))
    for i in range(1, n+1):
        if (px<len(s1) and s1[px] == i):
            # print elements of first set
            print(i, end=" ")
            px+=1
        else:
            # print remaining elements as the second set.
            s2.append(i)
    print()
    print(len(s2))
    print(' '.join(str(elem) for elem in s2))
    