a = int(input())
b = int(input())
def w(a ,b):
    return a*b
def r(a, b):
    return (a+b)*2
def rectangle(a, b):
    return (w(a,b), r(a,b))
print(rectangle(a,b))