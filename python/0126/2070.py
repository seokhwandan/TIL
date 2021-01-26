# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
# 3
# 3 8
# 7 7
# 369 123

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    n1, n2 = list(map(int, input().split()))
    if n1 > n2:
        print(f'#{t+1} >')
    elif n1 == n2:
        print(f'#{t+1} =')
    else:
        print(f'#{t+1} <')