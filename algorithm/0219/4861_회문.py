import sys
sys.stdin = open('4861.txt')

def my_reverse(line):
    r_line = []
    for i in range(len(line) - 1, -1, -1):
        r_line.append(line[i])
    return r_line

def my_find():
    # 전체크기가 N
    for i in range(N):
        # 가로 검사
        for j in range(N - M + 1):
            # 부분 문자열을 위한 빈 리스트
            tmp = []
            for k in range(M):
                tmp.append(words[i][j+k])
            if tmp == my_reverse(tmp):
                return tmp
        # 세로 검사
        for j in range(N - M + 1):
            tmp = []
            for k in range(M):
                tmp.append(words[j + k][i])
            if tmp == my_reverse(tmp):
                return tmp
    return []

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    ans = my_find()
    print('#{} {}'.format(t, ''.join(ans)))