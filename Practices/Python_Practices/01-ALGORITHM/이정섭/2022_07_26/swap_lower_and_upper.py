s = input()
li = [c.upper() if c.islower() else c.lower() for c in s]
print(''.join(li))