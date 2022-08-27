a,b = map(int, input().split())
d = dict()
for _ in range(a):
    n = input()
    d[n] = n
an = []
for _ in range(b):
    m = input()
    if m in d:
        an.append(m)
an.sort()
print(len(an))
for k in an:
    print(k)


# Alt 1

# N, M = map(int, input().split())

# answer = []
# hear = []
# saw = []

# for _ in range(N):
#     hear.append(input().rstrip())

# for _ in range(M):
#     saw.append(input().rstrip())

# hear = set(hear)
# saw = set(saw)

# answer = list(hear.intersection(saw))

# answer.sort()

# print(len(answer))

# for name in answer:
#     print(name)