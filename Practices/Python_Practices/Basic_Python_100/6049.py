# 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2

# 두 정수(a, b)를 공백으로 구분하여 입력받은 후 조건문을 통해 a와 b의 값이 같은 경우에는 True를 출력하고
# 반대로 그렇지 않을 경우에는 False를 출력한다.

a, b = input().split()

if int(a)==int(b):
  print("True")
else:
  print("False")