import sys
sys.stdin = open('1227.txt')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for t in range(10):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    r, c = 0, 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                r, c = i, j
    stack = [r, c]
    flag = 0
    while stack:
        sc = stack.pop()
        sr = stack.pop()
        arr[sr][sc] = 1
        for dr, dc in d:
            nr = sr + dr
            nc = sc + dc
            if 0 <= nr < 100 and 0 <= nc < 100:
                if arr[nr][nc] == 0:
                    stack.append(nr)
                    stack.append(nc)
                if arr[nr][nc] == 1:
                    continue
                if arr[nr][nc] == 3:
                    flag = 1
                    break
        if flag == 1:
            break
    print('#{} {}'.format(N, flag))