N = int(input())
arr = list(map(int, input().split()))

ways = [0]
# 오르막길만 추출(오르막길경우에 차이 추가, 내리막 혹은 같으면 0)
for i in range(len(arr)-1):
    diff = arr[i+1] - arr[i]
    if diff > 0:
        ways.append(diff)
    else:
        ways.append(0)

#이어지는 오르막 판별위해 sum을 이용
s1 = 0
new = [0]
for i in ways:
    if i > 0 :
        s1 += i
    else:
        new.append(s1)
        s1 = 0
new.append(s1)

print(max(new))