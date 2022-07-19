# 문제 21. 숫자 뒤집기
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# Alternative 2
# def reverse(s):
#     s = s[::-1]
#     return s
# s=input()
# print(reverse(s),type(reverse(s)))


n = int(input())
rst = 0
while n!=0:
    print(n%10, end='')
    n = n//10


# alterative 3
# number = int(input())

# result = 0

# while number != 0:
#     result += number % 10
#     number = number // 10
    

#     print(result,end="")
