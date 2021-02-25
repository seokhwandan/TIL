import sys
sys.stdin = open('4615.txt')

T = int(input())
d = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    m = N // 2
    board[m - 1][m - 1], board[m][m] = 2, 2
    board[m - 1][m], board[m][m - 1] = 1, 1
    for m in range(M):
        x, y, stone = map(int, input().split()) # x = c, y = r, board[y][x]
        x, y = x - 1, y - 1
        if board[y][x] == 0:
            board[y][x] = stone
        else:
            continue

        for i in range(1, N):
            for dr, dc in d:
                r = y + dr * i
                c = x + dc * i
                # 모서리 확인
                if r < 0 or c < 0 or r > N - 1 or c > N - 1:
                    continue
                # 어떠한 돌도 만나지 못했을 때
                if board[r][c] == 0:
                    break
                # 다른 색의 돌을 만났을 때
                if board[r][c] != stone:
                    continue
                # 같은 색의 돌을 만났을 때
                if board[r][c] == stone:
                    for j in range(1, i):
                        if board[y + dr * j][x + dc * j] == 0:
                            break
                        else:
                            r = y + dr * j
                            c = x + dc * j
                            board[r][c] = stone

    b, w = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == 2:
                w += 1
    print('#{} {} {}'.format(t, b, w))
