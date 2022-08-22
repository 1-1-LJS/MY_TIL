a = 0
b = [0, 0]
for c in input():
    if c == '@':
        b[a] += 1
    elif c == '(':
        a ^= 1
print(*b)


# Alt 1

# a,b=input().split("(^0^)")
# print(a.count('@'),b.count("@"))