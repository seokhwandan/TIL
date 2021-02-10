import sys
sys.stdin = open('1983.txt')

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    N, K = map(int, input().split())
    score_list = []
    for n in range(N):
        mid, final, hw = list(map(int, input().split()))
        # Print(mid, final, hw)
        score_list.append(mid*0.35 + final*0.45 + hw*0.2)

    score = score_list[K-1]
    score_list.sort(reverse=True)
    rank = score_list.index(score)
    # print(rank)
    
    res = grade[rank // (N // 10)]
    print(res)
    

    
    
        
        
    

