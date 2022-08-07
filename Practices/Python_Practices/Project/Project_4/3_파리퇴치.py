import sys

sys.stdin = open("_파리퇴치.txt")

# t = int(input())

# for tc in range(1, t + 1) :
#     n, m = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(n)]

#     result = 0
#     for i in range(n-m+1) :
#         for j in range(n-m+1) :
#             sum_value = 0
#             for k in range(m) :
#                 for l in range(m) :
#                     sum_value += board[i+k][j+l]
#             if sum_value > result :
#                 result = sum_value

#     print('#%d %d' % (tc, result))


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    n = M-1
    max_v = 0
    #N-M+1 범위의 idx만큼 순회
    for i in range(N-n):
        for j in range(N-n):
            sum_v = 0
            #해당 인덱스에서 MxM 범위 내 원소합을 저장
            for di in range(M):
                for dj in range(M):
                    sum_v += arr[i+di][j+dj]
            #최대값과 비교하며 최대값 저장
            if sum_v > max_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')
