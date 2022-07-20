import sys
sys.stdin = open('2050_input.txt')

s = input()
result = 0
for i in s:
    print(ord(i)-64, end='')
