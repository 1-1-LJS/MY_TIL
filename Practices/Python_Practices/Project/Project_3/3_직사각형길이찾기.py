t = int(input())
a,b,c = input().split()

# Undefined side 'd' is either a,b or c
# if a = b != c then d is c
# if a = b = c then d is a
# if a != b and a = c then d is b

def d(): 
    if a == b and a != c:
        print(c)
    elif a == c and a != b:
        print(b)
    elif a == b and a == c:
        print(a)
    return

for r in range (1, t+1): # range should be 1 to 't' and because python count from 0, it should be 't+1'
    print(f'#{r} {d()}')