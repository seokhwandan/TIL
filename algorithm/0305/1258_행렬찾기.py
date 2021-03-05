import sys
sys.stdin = open('1258.txt')

# 사각형의 크기를 찾아주는 함수
def search_size(r, c):
    row = 0
    col = 0

    # 행의 길이를 찾는
    for i in range(r, N):
        if arr[i][c]:
            row += 1
        else:
            break
    
    # 열의 길이를 찾는
    for i in range(c, N):
        if arr[r][i]:
            col += 1
        else:
            break

    size.append([row, col, row * col])
    init(r, c, row, col)

# 초기화
def init(r, c, row, col):
    for i in range(r, r + row):
        for j in range(c, c + col):
            arr[i][j] = 0

def counting_sort(idx):
    cnt = [0] * 10001
    sort_size = [0] * len(size)

    # 1. 카운팅 하는 과정
    for i in range(len(size)):
        cnt[size[i][idx]] += 1
    
    # 2. 누적
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]
    
    # 3. 정렬하여 넣는 과정
    for i in range(len(size) - 1, -1, -1):
        sort_size[cnt[size[i][idx]] - 1] = size[i]
        cnt[size[i][idx]] -= 1
    
    return sort_size

# T = int(input())
# for t in range(1, T + 1):
#     N = int(input()) # 2차원 list의 크기, N <= 100
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     size = []
#     # 행 우선순회 방식으로 순회하면서 사각형의 사각좌표를 구한다
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]:
#                 search_size(i, j)
#     ans = counting_sort(0) # 행을 기준으로 정렬
#     ans = counting_sort(2) # 행렬의 크기로 다시한번 정렬

#     print('#{} {}'.format(t, len(size)), end= ' ')
#     for i in range(len(size)):
#         print('{} {}'.format(size[i][0], size[i][1]), end= ' ')
#     print()

#####################################################################################

T = int(input())
for t in range(1, T + 1):
    N = int(input()) # 2차원 list의 크기, N <= 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    size = []
    # 행 우선순회 방식으로 순회하면서 사각형의 사각좌표를 구한다
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                r, c = i, j
                # 범위를 앞에 위치
                while r < N and arr[r][j]:
                    r += 1
                while c < N and arr[i][c]:
                    c += 1

                size.append([r - i, c - j])

                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0
    size.sort(key =lambda x : (x[0] * x[1], x[0]))
    print('#{} {}'.format(t, len(size)), end= ' ')
    for i in range(len(size)):
        print('{} {}'.format(size[i][0], size[i][1]), end= ' ')
    print()
