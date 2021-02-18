import sys
sys.stdin = open('이진탐색.txt')

def binary_search(a, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        if key == a[mid]:  # 검색 성공
            return cnt
        elif key < a[mid]:
            end = mid
        else:
            start = mid
    return -1  # 검색 실패

T = int(input())
for t in range(1, T + 1):
    P, A, B = map(int, input().split())
    arr = list(range(0, P + 1))
    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'
    else:
        ans = '0'

    print('#{} {}'.format(t, ans))
