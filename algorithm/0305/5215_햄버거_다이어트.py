import sys
sys.stdin = open('5215.txt')

# def sub(idx):
#     global max_score

#     if idx == N:
#         kcal = 0
#         score = 0   
#         for i in range(N):
#             if check[i]:
#                 score += arr[i][0]
#                 kcal += arr[i][1]
#         if kcal < L:
#             max_score = max(max_score, score)
#         return

#     check[idx] = 1
#     sub(idx + 1)
#     check[idx] = 0
#     sub(idx + 1)

def dfs(idx, total_score = 0, total_kcal = 0):
    global max_score
    if total_kcal > L:
        return

    if max_score < total_score:
        max_score = max(max_score, total_score)
    
    if idx == N:
        return
    
    score, kcal = arr[idx]
    dfs(idx + 1, total_score + score, total_kcal + kcal)
    dfs(idx + 1, total_score, total_kcal)

T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # check = [0] * N
    max_score = 0
    # sub(0)
    dfs(0)
    print('#{} {}'.format(t, max_score))

