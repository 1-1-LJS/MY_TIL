a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( not (c or d) )


# Alt 1
# a, b = map(int, input().split())
# a, b = bool(a), bool(b)

# if (a == False and b == False):
#     print("True")
# else:
#     print("False")
    