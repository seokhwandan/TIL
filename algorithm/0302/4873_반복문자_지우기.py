import sys
sys.stdin = open('4873.txt')

T = int(input())
for t in range(1, T + 1):
    stack = []
    str = input()
    for i in range(len(str)):
        # stack 이 비어있으면 push
        if not len(stack):
            stack.append(str[i])
        else:
            if stack[-1] == str[i]:
                stack.pop()
            else:
                stack.append(str[i])
    print('#{} {}'.format(t, len(stack)))