'''
C. Level Three (30%)

In this level, the program will first read a 5x5 bingo card, a roll (round) count
and n rows of strings. Each string contains 3 numbers as in level two. The
program should calculate all the possible numbers from 3 dice of each roll and
cross out the corresponding numbers on the bingo card. The number crossed
out should be replaced with a "x" mark.

Input:
6 + n lines of inputs

1st - 5th lines         The numbers on the 5 by 5 bingo card.
                        Each line contains 5 integers separated by a space.
6th line                Integer, n, numbers of rolls to be inputted.
7th - (7+n-1)th lines   n rows of roll.
                        Each row contains 3 integers separated by a space.

Output:
The numbers/marks on the bingo card in 5 by 5 grid. Each line should be
terminated by a line-feed character including the last line. Numbers/marks
will be printed in 4 characters width with right alignment. 
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

def card_printer(lis):
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if (lis[i][j] == "x") or (10 > lis[i][j] > 0):
                print("  ", lis[i][j], end=" ")
            else:
                print(" ", lis[i][j], end=" ")
        print()

# card_printer(bingo_lis)

poss_num_list, num_list = [], []
for roll in rolls:
    d1, d2, d3 = map(int, roll)
    # print(d1, d2, d3)
    poss_nums = sorted(set(r for _, r in part_two(d1, d2, d3) if r > 0))
    poss_num_list.append(poss_nums)
for a in poss_num_list:num_list+=a
dist_num_list = sorted(set(num_list))

bingo_num_list = []
for i in bingo_lis:bingo_num_list+=i

card_printer(bingo_lis)
print()

updated_bingo_num_list = ["x" if i in dist_num_list else i for i in bingo_num_list]
updated_bingo_list = [updated_bingo_num_list[i*5:(i+1)*5] for i in range((len(updated_bingo_num_list)+4)//5)]
# print(updated_bingo_list)
print(updated_bingo_list)
card_printer(updated_bingo_list)

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

   x    x    x    x    x 
  11    x    x    x    x 
   x   28    x    x   21 
   x    x    x    x    x 
   x    x    x   21    x 

'''