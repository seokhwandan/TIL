import sys
sys.stdin = open('5356.txt')

# # 글자 수 맞추기
# def customize(words):
#     # 가장 긴 문자열의 길이 찾기
#     max_len = 0
#     for word in words:
#         if max_len < len(word):
#             max_len = len(word)
#     # 문자열의 길이 맞추기
#     for i in range(len(words)):
#         if len(words[i]) < max_len:
#             words[i] += ' ' * (max_len - len(words[i]))
#     return words

# # 가로로 나열
# def row(words):
#     ans = ''    
#     for j in range(len(words[0])):
#         for i in range(len(words)):
#             if words[i][j] != ' ':
#                 ans += words[i][j]
#     return ans

def enumerate(words):
    new_word = ''
    for i in range(15):
        for j in range(5):
            if i < len(words[j]):
                new_word += words[j][i]
    return new_word

T = int(input())
for t in range(1, T + 1):
    words = [input() for _ in range(5)]
    # new = customize(words)
    # print('#{} {}'.format(t, row(new)))
    print('#{} {}'.format(t, enumerate(words)))