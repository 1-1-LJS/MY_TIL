N = int(input())
li = sorted(list(map(int, input().split())), reverse=True)
t = [li[i]-(N-i-1) for i in range(N)]
res = N + max(t) + 1
print(res)