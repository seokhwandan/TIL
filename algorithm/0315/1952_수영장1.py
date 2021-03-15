import sys
sys.stdin = open('1952.txt')

T = int(input())
for t in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    plan = list(map(int, input().split()))
    minV = y
    month = []
    for i in range(len(plan)):
        month.append(m if m < plan[i] * d else plan[i] * d)
    
    stack = [(0, 0)]
    while stack:
        idx, money = stack.pop()
        if idx >= 12:
            if money < minV and money:
                minV = money
        else:
            if plan[idx]:
                stack.append((idx + 1, money + month[idx]))
                stack.append((idx + 3, money + m3))
            else:
                stack.append((idx + 1, money))
    
    print('#{} {}'.format(t, minV))