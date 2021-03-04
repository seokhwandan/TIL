import sys
sys.stdin = open('5097.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    cnt = M % N
    i = 0
    while i < cnt:
        num.append(num.pop(0))
        i += 1
    print('#{} {}'.format(t, num[0]))