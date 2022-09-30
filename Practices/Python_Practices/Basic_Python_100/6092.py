stlist = list()

for i in range(24):
    stlist.append(0)
    
num = int(input())
numlist = input().split()

for i in range(num):
    stlist[int(numlist[i])] += 1
    
for i in range(1, len(stlist)):
    print(stlist[i], end=' ')



# Alt 1
#  
# n = int(input())
# a = input().split()

# for i in range(n) :
#   a[i] = int(a[i])

# d = []
# for i in range(24) :
#   d.append(0)

# for i in range(n) :
#   d[a[i]] += 1

# for i in range(1, 24) :
#   print(d[i], end=' ')

