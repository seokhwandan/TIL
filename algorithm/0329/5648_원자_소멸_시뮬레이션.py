import sys
sys.stdin = open('5648.txt')

from collections import deque

# 0, 1, 2, 3 일 때 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# energy 값을 통해 방문체크
# -1000 ~ 1000 까지 총 2000, 중간(0.5)에도 만날 수 있으므로 2배해서 0 ~ 4000 으로 조정
energy = [[0] * 4001 for _ in range(4001)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    q = deque()
    for n in range(N):
        arr = list(map(int, input().split()))

        # +1000 을 함으로써 -1000 ~ 1000 의 범위를 0 ~ 2000 으로 바꿈
        # 곱하기 2 를 함으로써 중간에서 만나는 경우를 고려해줌
				# arr[0] = x 좌표 : column, arr[1] = y 좌표 : row
        # y 좌표 : row 의 경우 상 = - 1, 하 = + 1 이므로, 최대값(4000)에서 뺀 값을 row 값으로 함(상하대칭)
        c, r = (arr[0] + 1000) * 2, 4000 - (arr[1] + 1000) * 2

        # 편의 상 arr[0] 을 y좌표 row, arr[1] 을 x좌표 column 으로 바꿔줌
        arr[0], arr[1] = r, c
        
        energy[arr[0]][arr[1]] = arr[3] # 현재 좌표에 각 energy 값을 넣어줌
        q.append(arr) # [row, column, direction, energy] enQueue 
    # print(q)
    e = 0 # 총 energy
    while q: # q 가 존재할 때
        for i in range(len(q)): # q 의 모든 index 순회
            t = q.popleft()
            nr, nc = t[0] + dr[t[2]], t[1] + dc[t[2]] # 0.5초 후 좌표
            if 0 <= nr <= 4000 and 0 <= nc <= 4000: # 이동가능한 범위
                if energy[t[0]][t[1]] == t[3]: # 현재 좌표의 energy 가 현재 원자의 energy와 같을 때
                    if energy[nr][nc] == 0: # 0.5초 후 좌표의 energy 가 0 일 때
                        energy[nr][nc] = t[3] # 0.5초 후 좌표의 energy 를 현재 원자의 에너지로 설정
                        energy[t[0]][t[1]] = 0 # 현재 좌표의 energy 초기화
                        t[0], t[1] = nr, nc # 현재좌표를 0.5초 후 좌표로 변경
                        q.append(t) # 0.5초 후 좌표 enQueue

                    else: # 0.5초 후 좌표의 energy 가 0 이 아닐 때, 즉, 0.5초 후 다른 원자와 충돌하는 경우
                        energy[nr][nc] += t[3] # 0.5초 후의 좌표에 방출되는 energy 의 합 더하기
                        energy[t[0]][t[1]] = 0 # 현재 좌표의 energy 초기화
                        # 0.5초 후 충돌함으로써 소멸되기 때문에 다음 좌표를 enQueue 할 필요가 없음
												# 참고로 0.5초 후의 좌표는 이미 위의 if문에서 enQueue 되어있음

                else: # 현재 좌표의 energy 가 현재 원자의 energy 와 다를 때, 즉, 충돌한 위치일 경우
                    e += energy[t[0]][t[1]] # 방출되는 energy 의 합을 총 energy 에 더하기
                    energy[t[0]][t[1]] = 0 # 현재 좌표, 즉, 충돌이 일어난 곳의 energy 초기화
                    # 현재 좌표가 충돌한 곳이기 때문에 다음 좌표를 enQueue 할 필요가 없음

    print('#{} {}'.format(tc, e))

