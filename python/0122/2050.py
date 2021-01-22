import sys
sys.stdin = open('input.txt', 'r')

alphabet = list(input())
for i in alphabet:
    print(int(ord(i)) - 64, end=' ')

