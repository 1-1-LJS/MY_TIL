# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

n = int(input())
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print (factorial)