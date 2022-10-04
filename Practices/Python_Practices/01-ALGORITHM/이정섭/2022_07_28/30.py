N = input().rstrip()

if "0" in N and sum(map(int, N)) % 3 == 0:
    print("".join(reversed(sorted(N))))
else:
    print(-1)




# Alt 1

# n = list(input())
# n.sort(reverse=True)
# sum = 0
# for i in n:
#     sum += int(i)
# if sum % 3 != 0 or "0" not in n:
#     print(-1)
# else:
#     print(''.join(n))