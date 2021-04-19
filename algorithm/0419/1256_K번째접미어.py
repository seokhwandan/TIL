import sys
sys.stdin = open('1256.txt')

def find(word):
    arr = []
    for i in range(len(word)):
        arr.append(word[i:])
    arr.sort()
    return arr[K - 1]


T = int(input())
for t in range(1, T + 1):
    K = int(input())
    word = input()
    print('#{} {}'.format(t, find(word)))