import sys
sys.stdin = open('특별한정렬.txt')

def selection(a):
    for i in range(10):
        idx = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if a[idx] < arr[j]:
                    idx = j
        else:
            for j in range(i + 1, N):
                if a[idx] > arr[j]:
                    idx = j
        a[i], a[idx] = a[idx], a[i]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    selection(arr)
    print('#{}'.format(t), end=' ')
    for i in range(10):
        print(arr[i], end= ' ')
    print()