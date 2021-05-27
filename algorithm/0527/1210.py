import sys
sys.stdin = open('1210.txt')

def search(arr, y):
    r = 99
    c = y
    d = [(-1, 0), (0, 1), (0, -1)]
    while r > 0:
        for dr, dc in d:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= 100 or nc < 0 or nc >= 100:
                continue

            if arr[nr][nc] == 1:
                arr[r][c] = 0
                r, c = nr, nc
    return c      

for t in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    x = 99
    y = ladder[99].index(2)

    print(f'#{t} {search(ladder, y)}')