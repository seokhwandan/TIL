# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    num = list(map(int, input().split()))
    avg = sum(num) // len(num)
    print('#{} {}'.format(t+1, avg))