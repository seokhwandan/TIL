import sys
sys.stdin = open('3055.txt')

from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs():
    # 고슴도치 먼저 체크 후, 물 체크
    while q:
        r, c = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[r][c] == '*':
                    if arr[nr][nc] == '.' or arr[nr][nc] == 'S':
                        arr[nr][nc] = '*'
                        q.append((nr, nc))
                
                if arr[r][c] == 'S':
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = 'S'
                        distance[nr][nc] = distance[r][c] + 1
                        q.append((nr, nc))

                    if arr[nr][nc] == 'D':
                        distance[nr][nc] = distance[r][c] + 1
                        return distance[tr][tc]
    return 'KAKTUS'

T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    # D : 비버의 굴, S : 고슴도치의 위치, . : 비어있는 곳, * : 물, X : 돌
    # 매 분마다 고슴도치 이동
    # 물도 매 분마다 비어있는 곳으로 확장
    arr = [list(input()) for _ in range(R)]
    distance = [[0] * C for _ in range(R)]
    q = deque()

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                # 고슴도치를 맨앞으로 // 고슴도치 먼저 체크
                q.appendleft((i, j))
            if arr[i][j] == '*':
                # 물은 여러 곳에 있을 수 있다.
                q.append((i, j))
            if arr[i][j] == 'D':
                # 비버의 굴의 좌표
                tr, tc = i, j

    print(bfs())
