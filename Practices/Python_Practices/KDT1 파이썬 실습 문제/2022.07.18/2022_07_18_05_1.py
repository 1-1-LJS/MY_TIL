# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [3, 10, 20, 40, 7, 5]

total = 0

for i in numbers:
    total = total + i
    avg = int(total / len(numbers))

print(avg)
