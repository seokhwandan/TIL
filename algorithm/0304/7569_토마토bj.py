import sys
sys.stdin = open('7569.txt')

from collections import deque

d = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]

def bfs(arr):
    for r in range(H):
        for c in range(N):
            for h in range(M):
                if arr[r][c][h] == 1:
                    q.append((r, c, h))

    while q:
        r, c, h = q.popleft()
        for dr, dc, dh in d:
            nr = r + dr
            nc = c + dc
            nh = h + dh
            if 0 <= nr < H and 0 <= nc < N and 0 <= nh < M:
                if arr[nr][nc][nh] == 0:
                    arr[nr][nc][nh] = arr[r][c][h] + 1
                    q.append((nr, nc, nh))

    res = check(arr)
    return res

def check(arr):
    ans = 0
    for r in range(H):
        for c in range(N):
            for h in range(M):
                if arr[r][c][h] == 0:
                    return -1
                else:
                    ans = max(ans, arr[r][c][h])
    return ans - 1

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()

print(bfs(box))

# T = int(input())
# for t in range(1, T + 1):
#     M, N, H = map(int, input().split())
#     box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
#     q = deque()
#     print(bfs(box))

# d = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]

# def bfs():
#     for r in range(H):
#         for c in range(N):
#             for h in range(M):
#                 if box[r][c][h] == 1:
#                     q.append((r, c, h))

#     while q:
#         r, c, h = q.pop(0)
#         for dr, dc, dh in d:
#             nr = r + dr
#             nc = c + dc
#             nh = h + dh
#             if 0 <= nr < H and 0 <= nc < N and 0 <= nh < M:
#                 if box[nr][nc][nh] == 0:
#                     box[nr][nc][nh] = box[r][c][h] + 1
#                     q.append((nr, nc, nh))

# def check():
#     ans = 0
#     for r in range(H):
#         for c in range(N):
#             for h in range(M):
#                 if box[r][c][h] == 0:
#                     return -1
#                 else:
#                     ans = max(ans, box[r][c][h])
#     return ans - 1

# M, N, H = map(int, input().split())
# box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# q = []

# T = int(input())
# for t in range(1, T + 1):
#     M, N, H = map(int, input().split())
#     box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
#     q = []

#     bfs()
#     res = check()
#     print(res)