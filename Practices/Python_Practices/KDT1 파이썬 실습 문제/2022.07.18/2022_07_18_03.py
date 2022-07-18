# 예제 05. [오류 해결] 숫자의 길이 구하기

# number = 22020718
# print(len(number))

# TypeError: object of type 'int' has no len()

number = 22020718
print(len(str(number)))