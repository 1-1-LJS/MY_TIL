T = int(input())

for _ in range(T):
    s = int(input())
    n = int(input())
    price = s
    
    for _ in range(n):
        q, p = map(int, input().split())
        price += q * p
        
    print(price)






# for _ in range(int(input())):
#     s = int(input())
#     for _ in range(int(input())):
#         q, p = map(int, input().split())
#         s += q*p
#     print(s)