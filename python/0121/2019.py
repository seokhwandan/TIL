# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for n in range(N + 1):
    print(2 ** n, end=' ')
    n += 1