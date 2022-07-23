T = int(input())
for i in range(T) :
    nums = map(int,input().split())
    res = list(n for n in nums)
    if res[0] == res[1]:
        print( f"#{i+1} =" )
    elif res[0] > res[1]:
        print( f"#{i+1} >" )
    else:
        print( f"#{i+1} <" )