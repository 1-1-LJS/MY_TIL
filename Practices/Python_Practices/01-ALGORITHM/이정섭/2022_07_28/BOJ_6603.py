def dfs(depth):
    if depth == 6:
        print(*num)
        return 
    for i in range(n):
        if check[i]:
            continue
        num.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        num.pop()
        for j in range(i+1, n):
            check[j] = 0
        
while 1:
    t = list(map(int, input().split()))
    n, nums = t[0], t[1:]
    if n == 0:
        break
    num = []
    check = [0]*n
    dfs(0)
    print()