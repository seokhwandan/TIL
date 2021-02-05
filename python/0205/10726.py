import sys
sys.stdin = open('10726.txt')

TC = int(input())
for tc in range(1, TC + 1):
    print(f'#{tc}', end=' ')
    N, M = list(map(int, input().split()))
    sm = bin(M).lstrip('0b')[::-1]
    if '1' * N == sm[:N]:
        print('ON')
    else:
        print('OFF')