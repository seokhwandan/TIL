import sys
sys.stdin = open('1974.txt')

T = int(input())
for t in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku)
    res = 1 # 초기 결과값
    # 가로, 세로 검증
    for i in range(9):
        check_r = 0
        check_c = 0
        for j in range(9):
            # 1 부터 9까지의 합은 45 이므로,
            check_r += sudoku[i][j]
            check_c += sudoku[j][i]
        if check_r != 45 or check_c != 45:
            res = 0
    # 3x3 크기 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = 0
            for r in range(3):
                for c in range(3):
                    check += sudoku[i + r][j + c]
            if check != 45:
                res = 0
    print('#{} {}'.format(t, res))