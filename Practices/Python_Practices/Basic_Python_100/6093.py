num = int(input())
numlist = input().split()

numlist.reverse()

for i in range(0,num):
    print(numlist[i], end=' ')


# Alt 1
#  
# n = int(input())
# a = input().split()

# for i in range(n) :
#   a[i] = int(a[i])

# for i in range(n-1, -1, -1):
#   print(a[i], end=' ')
