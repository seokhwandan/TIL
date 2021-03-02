import sys
sys.stdin = open('4880.txt')

def tournament(l, r):
    if card[l] == card[r]:
        return l
    if card[l] == 1:
        return r if card[r] == 2 else l
    elif card[l] == 2:
        return r if card[r] == 3 else l
    else:
        return r if card[r] == 1 else l

def divide(s, e):
    if s == e:
        return s
    left = divide(s, (s + e) // 2)
    right = divide((s + e) // 2 + 1, e)
    return tournament(left, right)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))
    start = 0
    end = N - 1
    print('#{} {}'.format(t, divide(start, end) + 1))