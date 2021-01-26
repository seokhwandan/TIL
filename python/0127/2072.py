# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    num = list(map(int, input().split()))

    res = list()
    for odd_t in num:
        if odd_t % 2 == 1:
            res.append(odd_t)

    print('#{} {}'.format(t + 1, sum(res)))

