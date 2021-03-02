import sys
sys.stdin = open('4866.txt')

def solve(str):
    global flag
    stack = []

    for i in range(len(str)):
        # 왼쪽괄호
        if str[i] == '{' or str[i] == '(':
            stack.append(str[i])
        #오른쪽괄호
        elif str[i] == '}' or str[i] == ')':
            # isEmpty
            if len(stack) == 0:
                flag = 0
                return
            else:
                temp = stack.pop()
            # 같은쌍인지 확인
            if str[i] == ')':
                if temp != '(':
                    flag = 0
                    return
            elif str[i] == '}':
                if temp != '{':
                    flag = 0
                    return
    if len(stack) != 0:
        flag = 0
        return
        
T = int(input())    
for t in range(1, T + 1):
    str = input()
    flag = 1
    solve(str)
    print('#{} {}'.format(t, flag))