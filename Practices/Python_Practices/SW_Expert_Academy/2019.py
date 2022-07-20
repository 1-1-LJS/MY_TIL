import sys
sys.stdin = open('2019_input.txt')

N = int(input())
answer = []
for number in range(N + 1):
    answer.append(2 ** number)
print(answer)