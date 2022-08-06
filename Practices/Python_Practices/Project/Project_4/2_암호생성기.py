import sys

sys.stdin = open("_암호생성기.txt")

T = 10
for t in range(1, T+1):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        t = queue.pop(0) - i
        if t <= 0:
            queue.append(0)
            break
        queue.append(t)
        i += 1

    print("#{} {} {} {} {} {} {} {} {}".format(tc, *queue))




# Alt 1

# import collections


# T = 10
# for t in range(1, T+1):
#     tc = int(input())
#     queue2 = collections.deque(list(map(int, input().split())), maxlen=8)

#     i = 1
#     while True:
#         if i > 5:
#             i = 1
#         t = queue2.popleft() - i
#         if t <= 0:
#             queue2.append(0)
#             break
#         queue2.append(t)
#         i += 1

#     print("#{}".format(tc), end=" ")
#     for q in queue2:
#         print("{}".format(q), end=" ")
#     print()
    # 출력형태는 여러가지로 할 수 있다.
    # print("#{}".format(tc), end=" ")
    # print(*queue2, end=" ")
    # print()