import sys
sys.stdin = open('4864.txt')

# def find(a, b):
#     if a in b:
#         return 1
#     else:
#         return 0

# def brouteforce(p, t):
#     for i in range(len(t) - len(p) + 1):
#         for j in range(len(p)):
#             if p[j] != t[i + j]:
#                 break
#     else:
#         return 1

def brouteforce(p, t):
    for i in range(len(t) - len(p) + 1):
        is_ok = True
        for j in range(len(p)):
            if p[j] != t[i + j]:
                is_ok = False
                break
        if is_ok:
            return 1

def brouteforce2(p, t):
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return 1
    else:
        return 0

T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    print(brouteforce2(str1, str2))