# import sys

# sys.stdin = open("_퍼펙트셔플.txt")

# t = int(input())

# for tc in range(1, t+1):

#     n = int(input())
#     card = list(input().split())
#     divided_1 = []
#     divided_2 = []
#     shuffled_deck = [] 

#     if n % 2 == 0:  # If it's an even numbers of cards, divide in half and append the cards in list divided_1 and 2 evenly
#                     # 
        

T = int(input())
 
for tc in range(1,1+T):
 
    # 단어 수
    n = int(input())
 
    # 단어
    words = list(map(str,input().split()))
 
    # 나뉘는 값
    median_num = n//2
 
    # 저장 공간
    res = []
 
    # 값을 추가할 위치 값
    idx = 1
 
    # 나누기
    # n이 짝수인 경우
    if n % 2 == 0:
 
        for q in range(n):
            if q < median_num:
                res.append(words[q])
            else:
                res.insert(idx,words[q])
                idx += 2
 
    else:
 
        for q in range(n):
            if q < median_num+1:
                res.append(words[q])
            else:
                res.insert(idx, words[q])
                idx += 2
 
 
    print('#{}'.format(tc), *res)