import sys
sys.stdin = open('1223.txt')

def postfix(s):
    stack = []
    ans = ''
    for i in s:
        if i in '*+':
            if stack != []:
                if prec[stack[-1]] >= prec[i]:
                    ans += stack.pop()
            stack.append(i)
        else:
            ans += i
    while stack != []:
        ans += stack.pop()
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

prec = {'*': 2, '+': 1}
for t in range(1, 11):
    l = int(input())
    tc = input()
    # print(postfix(tc))
    print('#{} {}'.format(t, cal(postfix(tc))))