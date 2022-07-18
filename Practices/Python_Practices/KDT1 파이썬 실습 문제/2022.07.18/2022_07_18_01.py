# Q 예제 03. [오류 해결] 입력 받기
# numbers = input().split()
# print(sum(numbers))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'

numbers = list(map(int, input().split()))
print(sum(numbers))