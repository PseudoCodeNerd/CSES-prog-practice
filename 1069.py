# Introductory Problems : Repetitions
#  https://cses.fi/problemset/task/1069/

# We take the first character, continue forward with incrementing our count
# if the subsequent chr is the same, else, take the next chr, initiate a new counter
# for it and continue. Finally take the max of all chrs counters.

s = str(input())
count, maxa, curr_char = 0, 0, s[0]
for i in range(len(s)):
    if s[i] == curr_char: count+=1
    else:
        maxa = max(maxa, count)
        # reinitilazing counter
        count = 1
        curr_char = s[i]
print(max(count, maxa))
