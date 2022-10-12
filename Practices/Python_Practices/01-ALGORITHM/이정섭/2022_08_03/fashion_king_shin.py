t = int(input())

for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)
 

# Alt 1

# from collections import Counter
# t = int(input())

# for i in range(t):
#     n = int(input())
#     wear = []
#     for j in range(n):
#         a, b = input().split()
#         wear.append(b)

#     wear_Counter = Counter(wear)
#     cnt = 1 # 각 종류마다 항목의 개수

#     for key in wear_Counter:
#         cnt *= wear_Counter[key] + 1

#     print(cnt-1)