import sys
sys.stdin = open('11767.txt')

def check(arr):
    if len(arr) < 3:
        return False

    if arr[-1] in arr[:-1]:
        if arr.count(arr[-1]) >= 3:
            return True

    else:
        if arr[-1] - 1 in arr[:-1]:
            if arr[-1] - 2 in arr[:-1] or arr[-1] + 1 in arr[:-1]:
                return True
        elif arr[-1] + 1 in arr[:-1] and arr[-1] + 2 in arr[:-1]:
            return True

    return False

T = int(input())
for t in range(1, T + 1):
    print('#{}'.format(t), end=' ')
    arr = list(map(int, input().split()))
    p1, p2 = [], []
    ans = 0
    for i in range(6):
        p1.append(arr[i * 2])
        if check(p1):
            print(1)
            break
        p2.append(arr[i * 2 + 1])
        if check(p2):
            print(2)
            break            
    if not check(p1) and not check(p2):
        print(0)