# Introductory Problems : Two Knights
#  https://cses.fi/problemset/task/1072/

# I couldn't figure out the math where https://math.stackexchange.com/a/3266324/700646 really 
# came to my help. We can look at this problem by finding ways when the two nights are threating each other 
# which will be only in either a 2x3 or 3x2 matric (symmetry) then subtract that from the possible combinations 
# in a nxn matrix. NEW MATH LEARNT. This was ingenuitive.

n = int(input())
for i in range(1, n+1):
    # total cases -> ((n**2)*(n**2-1))/2
    tot = ((i**2)*(i**2-1))//2
    # possibly (n-1)!/(n-3)!
    threat_cases = 4*(i-1)*(i-2)
    print(tot - threat_cases)