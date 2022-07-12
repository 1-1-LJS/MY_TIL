# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = [-10, -100, -30]
min_num = numbers[0]
for n in numbers:
    if min_num > n:
        min_num = n
print(min_num)