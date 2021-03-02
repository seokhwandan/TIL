import sys
sys.stdin = open('4874.txt')

def cal(s):
    stack = []
    for i in s:
        # 숫자 또는 '.' 인 경우 스택에 추가
        if i not in '*/+-':
            stack.append(i)
            # stack의 top 이 '.' 일 때
            if stack[-1] == '.':
                # '.' 과 숫자만 존재하면 숫자 리턴
                if len(stack) == 2:
                    return stack[0]
                # 그 외에 더 있을 경우 error
                else:
                    return 'error'
        else:
            try:
                # stack 에 쌓은 숫자 2개를 pop하여 연산 후 다시 push
                if i == '*':
                    stack.append(int(stack.pop(-2)) * int(stack.pop(-1)))
                elif i == '/':
                    stack.append(int(stack.pop(-2)) // int(stack.pop(-1)))
                elif i == '+':
                    stack.append(int(stack.pop(-2)) + int(stack.pop(-1)))
                elif i == '-':
                    stack.append(int(stack.pop(-2)) - int(stack.pop(-1)))
            # 에러 발생 시 error 리턴
            except:
                return 'error'

T = int(input())
for t in range(1, T + 1):
    postfix = input().split()
    print('#{} {}'.format(t, cal(postfix)))
