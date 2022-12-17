a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
t = min(a/d, b/e, c/f)
print(a-d*t, b-e*t, c-f*t)