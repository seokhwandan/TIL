import sys
sys.stdin = open('5207.txt')

def find():
    cnt = 0

    for i in range(len(B)):
        l, r = 0, N - 1
        flag = 0 # 번갈아 탐색하는지 체크

        while l <= r:
            m = (l + r) // 2
            
            if B[i] > A[m]:
                l = m + 1
                if flag == 1: # 오른쪽을 탐색하고 온 상태라면
                    break
                flag = 1 # 오른쪽 체크
            
            elif B[i] < A[m]:
                r = m - 1
                if flag == - 1: # 왼쪽을 탐색하고 온 상태라면
                    break
                flag = -1 # 왼쪽 체크

            if B[i] == A[m]:
                cnt += 1
                break
    return cnt

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    print('#{} {}'.format(t, find()))