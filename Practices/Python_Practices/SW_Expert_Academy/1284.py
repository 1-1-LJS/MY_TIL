# T = int(input())

# for test_case in range(1, T + 1):
#     P, Q, R, S, W = map(int, input().split())
#     A = W * P
#     if R > W:
#         B = Q
#     else:
#         B + Q + S*(W-R)
#     print(f'#{test_case}) {min(A, B)}')


T = int(input())
for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    cost_A = W * P 
    cost_B = Q
    if R < W:
        cost_B += S * (W-R)

    cost = min(cost_A, cost_B)

    print('#{} {}'.format(t, cost))