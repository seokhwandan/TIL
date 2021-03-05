import sys
sys.stdin = open('4613.txt')

def perm(idx, row):
    global min_value
    # 가지치기
    if row > N:
        return
    
    if idx == 3:
        if row == N:
            cnt = 0 # 값을 바꿔야되는 갯수를 세기위한 변수
            st = sel[0]
            st2 = st + sel[1]
            # 흰색 칠하기
            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt += 1
            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt += 1
            
            # 빨간색 칠하기
            for i in flag[st2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1
            
            if min_value > cnt:
                min_value = cnt
        return
    
    # 중복순열 살짝 응용
    for i in range(1, N - 1):
        sel[idx] = i
        perm(idx + 1, row + i)

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    sel = [0] * 3
    min_value = N * M + 1
    # 앞에는 idx, 뒤에는 중간 합
    perm(0, 0)
    print('#{} {}'.format(t, min_value))

##########################################################################

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    W = [0] * N
    B = [0] * N
    R = [0] * N
    # 행을 보면서 나와 다른 색의 갯수를 카운팅
    for i in range(N):
        for j in range(M):
            if flag[i][j] != 'W':
                W[i] += 1
            if flag[i][j] != 'B':
                B[i] += 1
            if flag[i][j] != 'R':
                R[i] += 1
    
    # 누적 시키기
    for i in range(1, N):
        W[i] += W[i - 1]
        B[i] += B[i - 1]
        R[i] += R[i - 1]
    
    ans = N * M + 1
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            wcnt = W[i]
            bcnt = B[j] - B[i]
            rcnt = R[N - 1] - R[j]

            if ans > wcnt + bcnt + rcnt:
                ans = wcnt + bcnt + rcnt
    print('#{} {}'.format(t, ans))

