import sys
sys.stdin = open('4869.txt')

def paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    return paper(n - 10) + paper(n - 20) * 2

T= int(input())
for t in range(1, T + 1):
    N = int(input())
    print("#{} {}".format(t, paper(N))) 