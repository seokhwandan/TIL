import sys
sys.stdin = open('2819.txt')

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs(r, c, case):
    
    if len(case) == 7:
        caselist.add(case)
        return
        
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, case + arr[nr][nc])

    

T = int(input())
for t in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    caselist = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c, arr[r][c])
    print('#{} {}'.format(t, len(caselist)))
