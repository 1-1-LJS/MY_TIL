import sys

sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
sys.stdin = open('input_1926.txt', 'r')

def dfs(r, c):
    global cnt

    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    if picture[r][c] == 1:
        cnt += 1
        picture[r][c] = 0
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r + 1, c)
        dfs(r, c - 1)
          
n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1] 
cnt = 0
area = []

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            cnt = 0
            dfs(i, j)
            area.append(cnt)

if area:
    print(len(area))
    print(max(area))
else:
    print(0)
    print(0)