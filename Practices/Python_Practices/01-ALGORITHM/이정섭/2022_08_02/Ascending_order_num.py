T = int(input())
n_list = []


for i in range(T):
    n_list.append(int(input()))

num_list = sorted(n_list)
for i in range(len(n_list)):
    print(num_list[i])