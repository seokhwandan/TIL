import sys
sys.stdin = open('1974.txt')

T = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    #print(N)
    puzzle = [list(map(int, input().split())) for p in range(9)]
    plist = []
    for v in range(0, 9, 3):
        for h in range(0, 9, 3):
            slist = []
            for sv in range(3):
                for sh in range(3):
                    slist.append(puzzle[v + sv][h + sh])
            plist.append(slist)
    # print(plist)
    
    hlist = []
    vlist = []
    for v in range(9):
        hp = []
        vp = []
        for h in range(9):
            hp.append(puzzle[h][v])
            vp.append(puzzle[v][h])
        hlist.append(hp)
        vlist.append(vp)
    
    hsum = 0
    vsum = 0
    psum = 0
    
    for pl in plist:
        if sorted(pl) == nums:
            psum += 1
        else:
            psum = 0

    for hl in hlist:
        if sorted(hl) == nums:
            hsum += 1
        else:
            hsum = 0
    
    for vl in vlist:
        if sorted(vl) == nums:
            vsum += 1
        else:
            vsum = 0

    if psum == 9 & hsum == 9 & vsum == 9:      
        print(1)
    else:
        print(0)