'''
A. Level One (10%)

In this level, the program will use the calculation mentioned above to generate
all possible numbers from the values of 2 dice, i.e. without op2 and dice3.

Input: Two integers separated by a space, which are the values of 2 dice.
e.g. 3 9

Output: A list of numbers and the corresponding calculations, sorted by the
number and then the calculation. Only number greater than zero should be
printed. Each line should be terminated by a line feed. The number and its
calculation are separated by a ":". In this part, duplicate expression should be
printed (for division only). 

For example, if 2, 2 are rolled, there should be two
2/2 expressions in the list. The order of operands in the calculation should be
same as the input order for +, - and * operators.
'''

# Order of precedence of operations for reference  : PEMDAS

op_lis = ["*", "/", "+", "-"]
d1, d2 = map(int, input().split())
cal_lis = []
for op in op_lis:
    if op == "*":
        cal = d1*d2
        s_cal = str(d1)+op+str(d2)
        if cal>0:cal_lis.append(str(cal)+":"+s_cal)
    if op == "/":
        if d1%d2 == 0:
            cal1 = int(d1/d2)
            s_cal1 = str(d1)+op+str(d2)
            cal_lis.append(str(cal1)+":"+s_cal1)
        if d2%d1 == 0:
            cal2 = int(d2/d1)
            s_cal2 = str(d2)+op+str(d1)
            cal_lis.append(str(cal2)+":"+s_cal2)
    if op == "+":
        cal = d1+d2
        s_cal = str(d1)+op+str(d2)
        if cal>0:cal_lis.append(str(cal)+":"+s_cal)
    if op == "-":
        if d1>d2:
            cal = d1-d2
            s_cal = str(d1)+op+str(d2)
            cal_lis.append(str(cal)+":"+s_cal)
        elif d2>d1:
            cal = d2-d1
            s_cal = str(d2)+op+str(d1)
            cal_lis.append(str(cal)+":"+s_cal)
        else:
            pass

def res_sort(s):
    return int(s.split(":")[0])

final = sorted(cal_lis, key=res_sort)
for result in final:
    print(result, end='\n')

'''
Case 5

Input:
18 9
Output:
2:18/9
9:18-9
27:18+9
162:18*9

All Cases Passed
'''