import sys
sys.stdin = open('4408.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    room = [0] * 200
    for i in range(N):
        start, end = map(int, input().split())
        if start % 2:
            start = start // 2
        else:
            start = start // 2 - 1
        if end % 2:
            end = end // 2
        else:
            end = end // 2 - 1

        if start < end:
            for j in range(start, end + 1):
                room[j] += 1
        else:
            for j in range(start, end - 1, -1):
                room[j] += 1
    print('#{} {}'.format(t, max(room)))
