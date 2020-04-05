# Introductory Problems : Permutations
#  https://cses.fi/problemset/task/1070/

# so on analysing the question we see that for n less than 4 (except 1 for there ans would be just 1)
# we have no possible cases and for n=4 there is only 1 probable case. for all other n, we can just 
# concatenate lists of even and odd nus/indices (since list is of natural numbers) into another list and be assured 
# that the difference of  subsequent sums wouldn't be 1.


n = int(input())
a = [f for f in range(1, n+1)]
e, o = [], []
if n == 1: print(1)
elif n < 4: print('NO SOLUTION')
elif n == 4: print('3 1 4 2')
else:
    for i in range(len(a)):
        if i%2==0: e.append(a[i])
        else: o.append(a[i])
    re = e + o 
    re = [str(r) for r in re]
    print(' '.join(re))

