# 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)

# 정수 2개(a, b)를 입력받아 a를 2^b배 만큼 곱한 값을 출력한다.
# 0 <= a <= 10, 0 <= b <= 10

a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)


# Alt 1

# a, b = map(int, input().split())
# c = 2**b

# print(a*c)