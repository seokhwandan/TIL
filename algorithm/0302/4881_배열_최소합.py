import sys
sys.stdin = open('4881.txt')

def perm(idx): # idx == 행
    global sum_value, min_value
    # 가지치기
    # 합이 최소값보다 클 경우 return
    if sum_value > min_value:
        return

    # 합이 최소값보다 작을 경우, 최소값 갱신
    if idx == N:
        if sum_value < min_value:
            min_value = sum_value
        return

    for i in range(N): # 열에 대해서
        # 방문체크
        if not check[i]:
            check[i] = 1
            # 합 구하기
            sum_value += arr[idx][i]
            perm(idx + 1) 
            check[i] = 0 # 다음 반복문을 위한 원상복구
            sum_value -= arr[idx][i]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N # 해당 열을 이미 사용했는지 안했는지에 대한 체크
    # 10 미만 자연수이므로, 최소 N * 1, 최대 N * 9
    sum_value = 0
    min_value = N * 9
    perm(0)
    print('#{} {}'.format(t, min_value))