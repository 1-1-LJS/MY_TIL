s = input()
c = 0
for i in s:
    if i == 'a':
        print(c)
        break
    elif not 'a' in s:
        print('-1')
        break
    else:
        c += 1

