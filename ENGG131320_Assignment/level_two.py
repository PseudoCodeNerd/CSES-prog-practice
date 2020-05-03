'''
B. Level Two (30%)

The program for this level is similar to level one but 3 dice are rolled.

Input: Three integers separated by a space, which are the numbers given by
rolling 3 dice.
e.g. 3 9 1

Output: A list of possible numbers separated by a space. The output should be
terminated by a space (instead of line feed). Duplicate number should be
removed.
'''

# #  ! Order of precedence of operations for reference  : PEMDAS !

# including grouping of operations in combinations using recursive function.
# with help from good fellows at Stack Overflow !

# d1, d2, d3 = map(int, input().split())

def part_two(*values):
    if len(values) == 2:
        a,b  = values
        sa,a = (f"({a[0]})",a[1]) if isinstance(a,tuple) else (str(a),a)
        sb,b = (f"({b[0]})",b[1]) if isinstance(b,tuple) else (str(b),b)
        yield f"{sa}+{sb}", a+b
        yield f"{sa}-{sb}", a-b
        yield f"{sb}-{sa}", b-a
        yield f"{sa}*{sb}", a*b
        # case for division
        if b != 0 and a%b==0: yield f"{sa}/{sb}", a//b
        if a != 0 and b%a==0: yield f"{sb}/{sa}", b//a
        return
    perms = ((i,j) for i in range(len(values)-1) for j in range(i+1,len(values))) 
    for i,j in perms:
        rem = [*values]
        a,b  = rem.pop(j), rem.pop(i)
        for paired in part_two(a,b):
            for result in part_two(paired, *rem):
               yield result

# printing distinct positive results.
# result = sorted(set(r for _, r in part_two(d1, d2, d3) if r > 0))

# for e in result:print(e, end=" ")

'''
All Cases Passed.

Eg. Input : 
11 5 2

Output :
1 3 4 8 12 14 17 18 21 27 32 33 45 53 57 65 77 110

See all other (non-functional) code attempts below...
'''

# # This time, there will be 4x4 = 16 total pairs of operations. Using Brute Force. Could also use itertools package.
# # This could be done more effectively by using a tree.

# # def div(x, y):
# #     if x!=0 and y!=0:
# #         if x%y==0:return x/y
# #         else:return None


# # ops_lis = ["**", "*/", "*+", "*-", "/*", "//", "/+", "/-", "+*", "+/", "++", "+-", "-*", "-/", "-+", "--"]

# # d1, d2, d3 = map(int, input().split())
# # cal_lis, res_lis = [], []
# # for op in ops_lis:
# #     if op[0] == "*" and op[1] == "*":cal_lis.append(d1*d2*d3)
# #     if op[0] == "*" and op[1] == "/":
# #         if div(d1*d2, d3) != None:cal_lis.append(div(d1*d2, d3))
# #         cal_lis.append(div(d1*d2, d3))
# #     if op[0] == "*" and op[1] == "+":
# #         cal_lis.append(d1*(d2+d3))
# #         cal_lis.append((d1*d2)+d3)
# #     if op[0] == "*" and op[1] == "-":
# #         cal_lis.append(abs(d1*d2-d3))
# #         cal_lis.append(abs(d1*(d2-d3)))
# #         cal_lis.append(abs((d1*d3)-d2))
# #     if op[0] == "/" and op[1] == "*":cal_lis.append(div(d1, d2*d3))
# #     if op[0] == "/" and op[1] == "/":
# #         if div(d1, d2) == None or div(d2, d3) == None:
# #             cal_lis.append(None)
# #         else:
# #             cal_lis.append(div(div(d1, d2), d3))
# #     if op[0] == "/" and op[1] == "+":
# #         if div(d1, d2) == None:
# #             cal_lis.append(None)
# #         else:
# #             cal_lis.append(div(d1, d2)+d3)
# #     if op[0] == "/" and op[1] == "-":
# #         if div(d1, d2) == None:
# #             cal_lis.append(None)
# #         else:
# #             cal_lis.append(div(d1, d2)-d3)
            
# #     if op[0] == "+" and op[1] == "*":
# #         cal_lis.append(d1+d2*d3)
# #         cal_lis.append((d1+d2)*d3)
# #         cal_lis.append((d1+d3)*d2)
# #     if op[0] == "+" and op[1] == "/":
# #         if div(d2, d3) == None:
# #             cal_lis.append(None)
# #         else:
# #             cal_lis.append(d1+div(d2, d3))
# #     if op[0] == "+" and op[1] == "+":cal_lis.append(d1+d2+d3)
# #     if op[0] == "+" and op[1] == "-":cal_lis.append(abs(d1+d2-d3))

# #     if op[0] == "-" and op[1] == "*":
# #         cal_lis.append(abs(d1-d2*d3))
# #         cal_lis.append(abs((d1-d2)*d3))
# #         cal_lis.append(abs((d1-d3)*d2))
# #     if op[0] == "-" and op[1] == "/":
# #         if div(d2, d3) == None:cal_lis.append(None)
# #         else: cal_lis.append(abs(d1-div(d2, d3)))
# #         if div(d1-d2, d3) == None:cal_lis.append(None)    
# #         else: cal_lis.append(abs(div(d1-d2, d3)))
# #     if op[0] == "-" and op[1] == "+":cal_lis.append(abs(d1-d2+d3))
# #     if op[0] == "-" and op[1] == "-":cal_lis.append(abs(d1-d2-d3))

# # print(cal_lis)
# # cal_lis = [int(cal) for cal in cal_lis if cal!=None]
# # for res in cal_lis:
# #     if (res > 0 and res not in res_lis):
# #         res_lis.append(int(res))
# # for a in sorted(res_lis):
# #     print(a, end=" ")
# from itertools import permutations
# ops = ['+', '-', '*', '/']
# nums = [11, 5, 2]

# # combos = permutations(nums, 2)
# # for expr in combos:
# #     for op in ops:
# #         if op == '/':
# #             if expr[0]%expr[1]==0:
# #                 eval_me = f'{expr[0]} {op} {expr[1]}'
# #                 result = eval(eval_me)
# #             if expr[1]%expr[0] == 0:
# #                 eval_me = f'{expr[1]} {op} {expr[0]}'
# #         else:
# #             eval_me = f'{expr[0]} {op} {expr[1]}' # make a string with num0 op num1
# #             result = eval(eval_me)

# #         print (f'{eval_me} = {result}')

# from itertools import product, permutations
# ops = ['+', '-', '*', '/']
# n = [3, 4, 1]
# num_perms = [list(p) for p in permutations(n)]
# print(num_perms)
# res_lis = []
# combos = product(ops, repeat=2)
# for nums in num_perms:
#     for expr in combos:
#         eval_1 = f'({nums[0]} {expr[0]} {nums[1]}) {expr[1]} {nums[2]}'
#         eval_2 = f'{nums[0]} {expr[0]} ({nums[1]} {expr[1]} {nums[2]})'
#         try:
#             res1 = eval(eval_1)
#             res_lis.append(res1)
#             print (f'{eval_1} = {res1}')
#             res2 = eval(eval_2)
#             res_lis.append(res2)
#             print(f'{eval_2} = {res2}')
#         except ZeroDivisionError as e:
#             print (f'expression  caused an exception: {e}')
# print(res_lis)

# from itertools import product, permutations
# ops = ['+', '-', '*', '/']
# n = [11, 5, 2]
# res_lis = []
# num_perms = [list(p) for p in permutations(n)] 
# print(num_perms)
# combos = product(ops, repeat=2)
# for i in range(len(num_perms)):
#     nums = num_perms[i]
#     for expr in combos:
#         eval_1 = f'({nums[0]} {expr[0]} {nums[1]}) {expr[1]} {nums[2]}'
#         eval_2 = f'{nums[0]} {expr[0]} ({nums[1]} {expr[1]} {nums[2]})'
#         try:
#             res_1= int(eval(eval_1))
#             res_lis.append(res_1)
#             print (f'{eval_1} = {res_1}')
#             res_2 = int(eval(eval_2))
#             res_lis.append(res_2)
#             print (f'{eval_2} = {res_2}')
#         except ZeroDivisionError as e:
#             print (f'expression caused an exception: {e}')
#     print(nums)
# final = []
# for e in res_lis:
#     if e>0 and e not in final:final.append(e)
# print(sorted(final))

