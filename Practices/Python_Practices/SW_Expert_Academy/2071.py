T = int(input())
for i in range(T) :
    nums = map(int,input().split())
    res = sum(n for n in nums)
    print( f"#{i+1} {round(res/10)}" )