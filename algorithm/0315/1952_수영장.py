import sys
sys.stdin = open('1952.txt')

def f(month, price):
    global minV
    if month >= 12:
        if price < minV:
            minV = price
    else:
        f(month + 1, price + d * plan[month])
        f(month + 1, price + m)
        f(month + 3, price + m3)

T = int(input())
for t in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    plan = list(map(int, input().split()))
    minV = y

    f(0, 0)
    print('#{} {}'.format(t, minV))