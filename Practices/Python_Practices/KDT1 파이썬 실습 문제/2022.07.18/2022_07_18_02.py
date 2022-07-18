# 예제 04. [오류 해결] 입력 받기 - 2

# words = list(map(int, input().split()))
# print(words)

# ValueError: invalid literal for int() with base 10: "i'm"

words = input().split()
print(words)