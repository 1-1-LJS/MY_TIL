# 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1

# 두 정수(a, b)를 공백으로 구분하여 입력받은 후 조건문을 통해 a가 b보다 작은 경우 True를 출력하고
# 반대로 b가 a보다 작은 경우 False를 출력한다.



a, b = input().split()

if int(a)<int(b):
  print("True")
else:
  print("False")