for _ in range(int(input())):
    s = input().split()
    n = float(s[0])
    for op in s[1:]:
        if op == '@':
            n *= 3
        elif op == '%':
            n += 5
        elif op == '#':
            n -= 7
    print("%.2f" % (n))