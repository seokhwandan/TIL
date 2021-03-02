import sys
sys.stdin = open('1224.txt')

prec = {'*': 2, '+': 1}

def postfix(s):
    stack = []
    ans = ''
    for i in s:
        if i not in '(*+)':
            ans += i
        else:
            if i in '(*+':
                stack.append(i)
                if i in prec.keys():
                    if stack[-2] in prec.keys():
                        if prec[stack[-2]] >= prec[i]:
                            ans += stack.pop(-2)
            elif i == ')':
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop() 
    return ans

def cal(s):
    num = []
    for i in s:
        if i not in '*+':
            num.append(i)
        else:
            if i == '+':
                num.append(int(num.pop(-2)) + int(num.pop(-1)))
            elif i == '*':
                num.append(int(num.pop(-2)) * int(num.pop(-1)))
    ans = num[0]
    return ans

for t in range(1, 11):
    n = int(input())
    txt = input()
    print('#{} {}'.format(t, cal(postfix(txt))))
