'''
D. Level Four (30%)

In this level, your program will find out at which roll (start from one) Bingo can
be claim. The program should read all the given input before the program end.

Input: Same as Level 3

Output:
Same as Level 3 if no Bingo could be claimed,
Otherwise, print out a string "Bingo! At round:N", where N is the Nth roll (start
from 1 to N) which lead to Bingo, followed by the snapshot of the bingo card
at time of Bingo.

In any case, only one bingo card will be printed.
'''

from level_two import part_two
# Comment out the two 'sys' lines below if you want to input from terminal.
import sys
sys.stdin = open('input.txt', 'r') 

# Input Space
bingo_lis, rolls = [], []
for _ in range(5):
    r = list(map(int, input().split()))
    bingo_lis.append(r)
num_rolls = int(input())
for _ in range(num_rolls):
    roll = list(map(int, input().split()))
    rolls.append(roll)

# print(bingo_lis, '\n', rolls)

def lis_unpack(lis):
    """convert lists of lists into a single list."""
    unpack_lis = []
    for sub_lis in lis:unpack_lis+=sub_lis
    return unpack_lis
 
def lis_repack(lis):
    """convert a single list into 5x5 bingo format"""
    return [lis[i*5:(i+1)*5] for i in range((len(lis)+4)//5)]

def card_printer(lis):
    """needs a list of lists 5x5. Use lis_repack"""
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if (lis[i][j] == "x") or (10 > lis[i][j] > 0):
                print("  ", lis[i][j], end=" ")
            else:
                print(" ", lis[i][j], end=" ")
        print()

def get_poss_nums(rolls_lis, rounds):
    """from list of roll lists, get poss_nums_list for current round"""
    poss_num_list = []
    for i in range(rounds):
        d1, d2, d3 = map(int, rolls_lis[i])
        poss_num_list.append(sorted(set(r for _, r in part_two(d1, d2, d3) if r > 0)))
    return sorted(set(lis_unpack(poss_num_list)))

def play_round(lis, r):
    """given unpacked list, update on the basis of poss_nums"""
    dist_num_list = get_poss_nums(rolls, r)
    return ["x" if i in dist_num_list else i for i in lis]

# print(get_poss_nums(rolls, num_rolls))
# card_printer(bingo_lis)

ind_criteria = [
    ('0 0','1 0','2 0','3 0','4 0'), ('0 1','1 1','2 1','3 1','4 1'), ('0 2','1 2','2 2','3 2','4 2'), 
    ('0 3','1 3','2 3','3 3','4 3'), ('0 4','1 4','2 4','3 4','4 4'), ('0 0','0 1','0 2','0 3','0 4'),
    ('3 0','3 1','3 2','3 3','3 4'), ('1 0','1 1','1 2','1 3','1 4'), ('2 0','2 1','2 2','2 3','2 4'),
    ('4 0','4 1','4 2','4 3','4 4'), ('0 4','1 3','2 2','3 1','4 0'), ('0 0','1 1','2 2','3 3','4 4')
]

def bingo_check(curr_state_list):
    """unpacked state list, print bingo or not"""
    state = lis_repack(curr_state_list)
    bings = 0
    for comb in ind_criteria:
        c = 0
        for ind in comb:
            i, j = ind.split(' ', 1)
            if state[int(i)][int(j)] == "x":c+=1
        if c==5:bings+=1
    if bings>=1:return True
    else:return False

global bingo
bingo = False
for ro in range(1, num_rolls+1):
    updated_bingo_num_list = play_round(lis_unpack(bingo_lis), ro)
    bingo = bingo_check(updated_bingo_num_list) 
    if bingo==True:
        break
if bingo:
    print('Bingo! At round:{}'.format(ro))
    card_printer(lis_repack(updated_bingo_num_list))
else:
    card_printer(lis_repack(updated_bingo_num_list))

'''
All Tests Passed.
Sample Input: 

1 2 3 4 5
11 10 13 14 15
26 28 29 25 21
5 3 2 1 4
15 13 14 21 26
4
5 1 3
6 11 8
6 5 4
10 1 3

Ouput:

Bingo! At round:3
   x    x    x    x    x 
  11    x    x    x    x 
   x   28    x    x   21 
   x    x    x    x    x 
   x    x    x   21    x 

'''

"""For Debugging"""
# card_printer(bingo_lis)
# print(play_round(lis_unpack(bingo_lis), 2))
# print(lis_repack(play_round(lis_unpack(bingo_lis), 2)))
# card_printer(lis_repack(play_round(lis_unpack(bingo_lis), 2)))
# bingo_check(play_round(lis_unpack(bingo_lis), 2))
