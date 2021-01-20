# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    n1, n2 = list(map(int, input().split(" ")))
    print('#{} {} {}'.format(t+1, n1 // n2, n1 % n2))