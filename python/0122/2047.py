# 신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.
# 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.
# The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.

import sys
sys.stdin = open('input.txt', 'r')

small = list(input())
for s in small:
    if ord(s) > 96:
        print(chr(ord(s) - 32), end='')
    else:
        print(s, end='')
