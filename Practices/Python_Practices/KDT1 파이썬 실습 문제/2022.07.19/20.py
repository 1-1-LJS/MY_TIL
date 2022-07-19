# 문제 20. 각 자릿수의 합 구하기

n = int(input())
def solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer
print(solution(n))